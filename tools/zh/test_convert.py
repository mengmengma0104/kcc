# -*- coding: utf-8 -*-
"""End-to-end conversion test across all output formats.

Generates a small synthetic comic, packs it as CBZ, then runs the CLI converter
for each output format and asserts that a usable artifact was produced. MOBI
additionally exercises the external kindlegen tool when present.

Usage:  <venv>\\Scripts\\python.exe tools/zh/test_convert.py
Exit code 0 = every format converted successfully.
"""
import os
import subprocess
import sys
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
WORK = os.path.join(ROOT, 'testdata')
SRC = os.path.join(WORK, 'pages')
OUT = os.path.join(WORK, 'out')
CBZ = os.path.join(WORK, 'test.cbz')

PYTHON = sys.executable
C2E = os.path.join(ROOT, 'kcc-c2e.py')

# 目标设备 / 输出格式 / 期望的产物扩展名
CASES = [
    ('KPW5', 'CBZ', '.cbz'),
    ('KPW5', 'PDF', '.pdf'),
    ('KPW5', 'EPUB', '.epub'),
    ('KoLC', 'EPUB', '.kepub.epub'),   # Kobo 配置 + EPUB 输出 => KEPUB
    ('KPW5', 'MOBI', '.mobi'),         # 需要 kindlegen
]


def make_input():
    """Create a small synthetic comic (6 pages) and pack it as CBZ."""
    from PIL import Image, ImageDraw

    os.makedirs(SRC, exist_ok=True)
    os.makedirs(OUT, exist_ok=True)
    for i in range(1, 7):
        p = os.path.join(SRC, 'page_%03d.png' % i)
        if os.path.exists(p):
            continue
        im = Image.new('L', (1200, 1800), 255)
        d = ImageDraw.Draw(im)
        d.rectangle([60, 60, 1140, 1740], outline=0, width=6)
        d.rectangle([140, 200, 1060, 700], outline=0, width=3)
        d.ellipse([300, 850, 900, 1450], outline=0, width=4)
        d.text((150, 120), 'PAGE %d' % i, fill=0)
        d.rectangle([140, 1500, 1060, 1650], fill=180)
        im.save(p)

    with zipfile.ZipFile(CBZ, 'w', zipfile.ZIP_DEFLATED) as z:
        for i in range(1, 7):
            z.write(os.path.join(SRC, 'page_%03d.png' % i), 'page_%03d.png' % i)
    print('input CBZ: %s (%d bytes)' % (CBZ, os.path.getsize(CBZ)))


def run_case(profile, fmt, expected_ext):
    """Convert with the given profile/format; return (ok, detail)."""
    before = set(os.listdir(OUT))
    cmd = [PYTHON, C2E, '-p', profile, '-f', fmt, '-o', OUT, CBZ]

    # kindlegen 可能位于分发目录、本地 dist、或系统已装 Kindle Previewer
    env = dict(os.environ)
    kg_dirs = [
        os.path.join(ROOT, 'dist'),
        r'D:\tool\KCC_11.2.0_zh',          # 便携分发目录（含 kindlegen.exe）
        os.path.expandvars(r'%LOCALAPPDATA%\Amazon\Kindle Previewer 3\lib\fc\bin'),
    ]
    for d in kg_dirs:
        if os.path.isdir(d):
            env['PATH'] = d + os.pathsep + env.get('PATH', '')

    try:
        p = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8',
                           errors='replace', cwd=ROOT, timeout=900, env=env)
    except subprocess.TimeoutExpired:
        return False, 'timeout'

    produced = [f for f in set(os.listdir(OUT)) - before if f.endswith(expected_ext)]
    if p.returncode == 0 and produced:
        size = os.path.getsize(os.path.join(OUT, produced[0]))
        return True, '%s (%d bytes)' % (produced[0], size)
    tail = (p.stdout or '')[-300:] + (p.stderr or '')[-300:]
    return False, 'rc=%s produced=%s | %s' % (p.returncode, produced, tail.strip())


def main():
    os.makedirs(OUT, exist_ok=True)
    make_input()

    results = []
    for profile, fmt, ext in CASES:
        label = '%s + %s' % (profile, fmt)
        ok, detail = run_case(profile, fmt, ext)
        print('%-14s %s  %s' % (label, 'OK  ' if ok else 'FAIL', detail))
        results.append((label, ok, detail))

    print()
    failed = [r for r in results if not r[1]]
    print('%d/%d formats OK' % (len(results) - len(failed), len(results)))
    if failed:
        print('failed:')
        for label, _, detail in failed:
            print('  -', label, detail)
        print('\nnote: MOBI 需要 kindlegen（Kindle Previewer 或 dist/kindlegen.exe）')
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
