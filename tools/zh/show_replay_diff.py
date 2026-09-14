# -*- coding: utf-8 -*-
"""Show exactly which lines differ between a replayed file and the working tree.

Diagnostic helper for verify_replay.py: when replay cannot reproduce a file
byte-for-byte, this prints the differing lines so the missing changes can be
folded back into the translation table or the applier.

Usage:  <venv>\\Scripts\\python.exe tools/zh/show_replay_diff.py <relpath> [<relpath> ...]
"""
import difflib
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


def safe_extract(archive, dest):
    """Write archive members one by one, refusing anything outside `dest`."""
    dest_real = os.path.realpath(dest)
    for info in archive.infolist():
        if info.filename.endswith('/'):
            continue
        target = os.path.realpath(os.path.join(dest_real, info.filename))
        if not target.startswith(dest_real + os.sep):
            raise SystemExit('zip 含越界路径，已拒绝: %s' % info.filename)
        os.makedirs(os.path.dirname(target), exist_ok=True)
        with archive.open(info) as src, io.open(target, 'wb') as out:
            shutil.copyfileobj(src, out)


def main():
    if len(sys.argv) < 2:
        print('用法: show_replay_diff.py <相对路径> [...]')
        return 2

    tmp = tempfile.mkdtemp(prefix='kcc-diff-')
    try:
        with zipfile.ZipFile(ZIP) as z:
            safe_extract(z, tmp)
        root_name = [d for d in os.listdir(tmp) if os.path.isdir(os.path.join(tmp, d))][0]
        upstream = os.path.join(tmp, root_name)

        env = dict(os.environ)
        env['KCC_REPLAY_ROOT'] = upstream
        env['PYTHONIOENCODING'] = 'utf-8'
        subprocess.run([sys.executable, os.path.join(TOOLS, 'apply_zh.py')],
                       capture_output=True, env=env, cwd=TOOLS)

        for rel in sys.argv[1:]:
            a = os.path.join(upstream, rel.replace('/', os.sep))
            b = os.path.join(ROOT, rel.replace('/', os.sep))
            print('=' * 70)
            print('文件:', rel)
            print('=' * 70)
            if not (os.path.exists(a) and os.path.exists(b)):
                print('  缺少文件: replay=%s worktree=%s' % (os.path.exists(a), os.path.exists(b)))
                continue
            la = io.open(a, encoding='utf-8').read().splitlines()
            lb = io.open(b, encoding='utf-8').read().splitlines()
            diff = list(difflib.unified_diff(la, lb, 'replay', 'worktree', lineterm='', n=2))
            if not diff:
                print('  完全一致')
            else:
                print('  差异行数: %d' % len(diff))
                for line in diff[:120]:
                    print('  ' + line)
                if len(diff) > 120:
                    print('  ...（共 %d 行，已截断）' % len(diff))
            print()
        return 0
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == '__main__':
    sys.exit(main())
