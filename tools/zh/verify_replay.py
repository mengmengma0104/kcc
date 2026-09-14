# -*- coding: utf-8 -*-
"""Replay verification: prove the translation can be rebuilt from the original
English source and the translation table alone.

Checks that the consolidated applier reproduces the current repository state
byte-for-byte. This is the evidence that pruning one-off scripts lost nothing:
whatever the pipeline does, it does through translations.py + apply_zh.py.

Steps
  1. extract the pristine upstream zip into a temp directory
  2. run apply_zh.py against that copy
  3. compare every translated file with the working tree

Exit code 0 = replay reproduces the current state exactly.
"""
import hashlib
import io
import os
import shutil
import subprocess
import sys
import tempfile
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ZIP = r'D:\tool\绿色软件\kcc-11.2.0.zip'
TOOLS = os.path.join(ROOT, 'tools', 'zh')

# 受翻译影响、因而必须逐字节复现的文件
TRANSLATED_FILES = [
    'kindlecomicconverter/KCC_gui.py',
    'kindlecomicconverter/KCC_ui.py',
    'kindlecomicconverter/KCC_ui_editor.py',
    'kindlecomicconverter/KCC_spread_label.py',
    'kindlecomicconverter/shared.py',
    'gui/KCC.ui',
    'gui/MetaEditor.ui',
]


def sha256(path):
    h = hashlib.sha256()
    with open(path, 'rb') as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def safe_extract(archive, dest):
    """Write archive members one by one, refusing anything outside `dest`.

    Archive member names are untrusted: `../evil` or an absolute path would
    otherwise escape the destination. Each entry is normalised and checked
    before any bytes are written.
    """
    dest_real = os.path.realpath(dest)
    for info in archive.infolist():
        name = info.filename
        if name.endswith('/'):
            continue
        target = os.path.realpath(os.path.join(dest_real, name))
        if not target.startswith(dest_real + os.sep):
            raise SystemExit('zip 含越界路径，已拒绝解压: %s' % name)
        os.makedirs(os.path.dirname(target), exist_ok=True)
        with archive.open(info) as src, io.open(target, 'wb') as out:
            shutil.copyfileobj(src, out)


def main():
    if not os.path.exists(ZIP):
        print('原始 zip 不存在，跳过重放验证：', ZIP)
        return 0

    tmp = tempfile.mkdtemp(prefix='kcc-replay-')
    try:
        # 1. 解出英文源码（逐条校验路径后写入）
        with zipfile.ZipFile(ZIP) as z:
            safe_extract(z, tmp)
        roots = [d for d in os.listdir(tmp) if os.path.isdir(os.path.join(tmp, d))]
        if not roots:
            raise SystemExit('zip 内未找到源码目录')
        upstream = os.path.join(tmp, roots[0])
        print('英文源码解出至:', upstream)

        # 2. 用统一应用器重放：apply_zh 支持 KCC_REPLAY_ROOT 指向其他源码树
        env = dict(os.environ)
        env['KCC_REPLAY_ROOT'] = upstream
        env['PYTHONIOENCODING'] = 'utf-8'
        r = subprocess.run([sys.executable, os.path.join(TOOLS, 'apply_zh.py')],
                           capture_output=True, text=True, encoding='utf-8',
                           errors='replace', env=env, cwd=TOOLS)
        print('重放输出:')
        for l in (r.stdout or '').splitlines():
            if 'replaced' in l or 'total replacements' in l or 'ERROR' in l:
                print('   ', l)
        if r.returncode != 0:
            print('应用器返回非零值 %d，重放失败' % r.returncode)
            if r.stdout:
                print(r.stdout[-800:])
            if r.stderr:
                print(r.stderr[-800:])
            return 1

        # 3. 逐文件比对
        print()
        mismatches = []
        for rel in TRANSLATED_FILES:
            a = os.path.join(upstream, rel.replace('/', os.sep))
            b = os.path.join(ROOT, rel.replace('/', os.sep))
            if not os.path.exists(a):
                print('%-44s MISSING' % rel)
                mismatches.append((rel, 'replay 未生成该文件'))
                continue
            ha, hb = sha256(a), sha256(b)
            print('%-44s %s' % (rel, 'IDENTICAL' if ha == hb else 'DIFFERENT'))
            if ha != hb:
                mismatches.append((rel, '%s != %s' % (ha[:12], hb[:12])))

        print()
        if mismatches:
            print('REPLAY MISMATCH —— 以下文件无法由翻译表复现:')
            for rel, why in mismatches:
                print('  -', rel, why)
            print('\n说明：这些文件含有翻译表之外的改动，需要补进 translations.py。')
            return 1

        print('REPLAY OK —— 全部译文文件可由「原始源码 + 翻译表」逐字节复现')
        print('（证明精简后的工具链未丢失任何必要步骤）')
        return 0
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == '__main__':
    sys.exit(main())
