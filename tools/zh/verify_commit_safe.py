# -*- coding: utf-8 -*-
"""预提交守卫：检查仓库中是否混入了不该提交的文件。

被拒绝的理由有两类：
  1. 许可 —— `kindlegen.exe` 是亚马逊专有软件，不允许再分发，绝不能入库。
  2. 卫生 —— 构建产物与二进制（exe/dll/压缩包/电子书）属于 Release 附件，
     不应留在源码树中。

位图资源只允许位于素材目录（icons/、images/、docs/），那里存放上游美术资源
与项目截图。

检查对象是 **git 索引**（即真正会入库的文件），因此自动遵循 .gitignore；
未跟踪的临时文件（测试数据、缓存）不会误报。

用法：  <venv>\\Scripts\\python.exe tools/zh/verify_commit_safe.py
退出码 0 = 没有禁止提交的文件。
"""
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
GIT = r'E:\Program Files\Git\cmd\git.exe'

# 这些扩展名一律不允许出现在仓库中（可执行文件、库、压缩包、电子书）
HARD_BAD_EXT = ('.exe', '.dll', '.pyd', '.so', '.dylib', '.dmg', '.appimage',
                '.zip', '.rar', '.7z', '.mobi', '.epub', '.cbz', '.pdf', '.msi')
# 位图资源仅允许放在这些目录下（上游素材与项目截图）
IMAGE_ALLOWED_PREFIX = ('icons/', 'images/', 'docs/')
# 上游自带、位于根目录的矢量资源（AppImage 图标）
IMAGE_ALLOWED_EXACT = {'application-vnd.appimage.svg'}
IMAGE_EXT = ('.png', '.jpg', '.jpeg', '.bmp', '.ico', '.icns', '.xcf', '.svg')


def tracked_files():
    """Return the list of files in the git index (those actually committed)."""
    raw = subprocess.run([GIT, '-C', ROOT, 'ls-files'],
                         capture_output=True, check=True)
    return [p.replace('\\', '/') for p in raw.stdout.decode('utf-8', 'replace').splitlines()
            if p.strip()]


def main():
    files = []
    for rel in tracked_files():
        full = os.path.join(ROOT, rel.replace('/', os.sep))
        size = os.path.getsize(full) if os.path.exists(full) else 0
        files.append((rel, size))
    files.sort()

    total = sum(s for _, s in files)
    print('已入库文件   : %d' % len(files))
    print('总体积       : %.2f MB' % (total / 1048576))

    violations = []
    for rel, size in files:
        low = rel.lower()
        if 'kindlegen' in os.path.basename(low):
            violations.append((rel, size, 'KINDLEGEN（许可不允许再分发）'))
        elif low.endswith(HARD_BAD_EXT):
            violations.append((rel, size, '可执行/压缩包/电子书'))
        elif low.endswith(IMAGE_EXT) and not low.startswith(IMAGE_ALLOWED_PREFIX) \
                and rel not in IMAGE_ALLOWED_EXACT:
            violations.append((rel, size, '位图资源不在允许目录内'))

    images = sum(1 for rel, _ in files if rel.lower().endswith(IMAGE_EXT))
    print()
    if violations:
        print('=== 禁止提交的文件 ===')
        for rel, size, why in violations:
            print('  [%s] %s (%d bytes)' % (why, rel, size))
        print()
        print('VERDICT: 需处理 %d 个文件' % len(violations))
        return 1

    print('VERDICT: 检查通过 —— 无 kindlegen、无可执行文件、无越界资源')
    print('（%d 个位图资源位于允许目录：icons/ images/ docs/）' % images)
    return 0


if __name__ == '__main__':
    sys.exit(main())
