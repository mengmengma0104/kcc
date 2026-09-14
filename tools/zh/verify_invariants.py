# -*- coding: utf-8 -*-
"""Verify the display-text / internal-key separation is intact.

The localization depends on two structures keeping their original English keys
while the combo boxes only display Chinese:
  * KCC_gui.self.profiles / self.formats — dict keys are internal identifiers
    used for lookups; translating them would break every conversion.
  * profilesGUI — the ordered source list that drives combo population; its
    order and length must stay stable because QSettings stores selection by index.

Also checks that no combo lookup still reads displayed text (currentText) instead
of the userData key (currentData).

Exit code 0 = all invariants hold.
"""
import ast
import io
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TARGET = os.path.join(ROOT, 'kindlecomicconverter', 'KCC_gui.py')

EXPECTED_FORMATS = [
    "MOBI/AZW3", "EPUB", "CBZ", "Folder of images", "PDF", "PDF (200MB limit)",
    "KFX (Send to Kindle EPUB)", "MOBI + EPUB", "EPUB (200MB limit)",
    "MOBI + EPUB (200MB limit)",
]
EXPECTED_PROFILES = [
    "Kindle Oasis 9/10", "Kindle 8/10", "Kindle Oasis 8", "Kindle Voyage",
    "Kindle 1860x1920", "Kindle 1920x1920", "Kindle 1240x1860", "Kindle 1324x1986",
    "Kindle Scribe 1/2", "Kindle Scribe 3", "Kindle Scribe Colorsoft", "Kindle 11",
    "Kindle Paperwhite 11", "Kindle Paperwhite 12", "Kindle Colorsoft",
    "Kindle Paperwhite 7/10", "Kindle Paperwhite 5/6", "Kindle 4/5/7", "Kindle DX",
    "Kobo Mini/Touch", "Kobo Glo", "Kobo Glo HD", "Kobo Aura", "Kobo Aura HD",
    "Kobo Aura H2O", "Kobo Aura ONE", "Kobo Clara HD", "Kobo Libra H2O", "Kobo Forma",
    "Kindle 1", "Kindle 2", "Kindle Keyboard", "Kindle Touch", "Kobo Nia",
    "Kobo Clara 2E", "Kobo Clara Colour", "Kobo Libra 2", "Kobo Libra Colour",
    "Kobo Sage", "Kobo Elipsa", "reMarkable 1", "reMarkable 2",
    "reMarkable Paper Pro", "reMarkable Paper Pro Move", "Other",
]
EXPECTED_GUI_LEN = 50
EXPECTED_SEPARATORS = 5


def main():
    src = io.open(TARGET, encoding='utf-8').read()
    tree = ast.parse(src)

    found_formats = found_profiles = found_gui = None
    for node in ast.walk(tree):
        if not isinstance(node, ast.Assign):
            continue
        for t in node.targets:
            if isinstance(t, ast.Attribute) and t.attr == 'formats' \
                    and isinstance(node.value, ast.Dict):
                found_formats = [k.value for k in node.value.keys if isinstance(k, ast.Constant)]
            if isinstance(t, ast.Attribute) and t.attr == 'profiles' \
                    and isinstance(node.value, ast.Dict):
                found_profiles = [k.value for k in node.value.keys if isinstance(k, ast.Constant)]
            if isinstance(t, ast.Name) and t.id == 'profilesGUI' \
                    and isinstance(node.value, ast.List):
                found_gui = [e.value for e in node.value.elts
                             if isinstance(e, ast.Constant) and isinstance(e.value, str)]

    failures = []

    print('formats keys : %d (expect %d)' % (len(found_formats or []), len(EXPECTED_FORMATS)))
    if found_formats != EXPECTED_FORMATS:
        failures.append('formats keys changed')
        print('  got     :', found_formats)
        print('  expected:', EXPECTED_FORMATS)

    print('profiles keys: %d (expect %d)' % (len(found_profiles or []), len(EXPECTED_PROFILES)))
    if found_profiles != EXPECTED_PROFILES:
        failures.append('profiles keys changed')
        print('  missing:', [k for k in EXPECTED_PROFILES if k not in (found_profiles or [])])
        print('  extra  :', [k for k in (found_profiles or []) if k not in EXPECTED_PROFILES])

    gui = found_gui or []
    print('profilesGUI  : len=%d, Separator=%d, first=%r'
          % (len(gui), gui.count('Separator'), gui[0] if gui else None))
    if len(gui) != EXPECTED_GUI_LEN:
        failures.append('profilesGUI length changed (%d != %d)' % (len(gui), EXPECTED_GUI_LEN))
    if gui.count('Separator') != EXPECTED_SEPARATORS:
        failures.append('profilesGUI separator count changed')
    if 'Other' not in gui:
        failures.append("profilesGUI lost the 'Other' entry")

    # 逻辑键必须保持 ASCII（中文会破坏查表）
    non_ascii = [k for k in (found_formats or []) + (found_profiles or [])
                 if any(ord(c) > 127 for c in k)]
    print('non-ascii keys:', non_ascii or '(none)')
    if non_ascii:
        failures.append('non-ASCII keys in lookup dicts: %r' % non_ascii)

    # 下拉框查找必须走 currentData()，不能读显示文字
    n_current = src.count('currentData()')
    n_text = src.count('deviceBox.currentText') + src.count('formatBox.currentText')
    print('currentData() sites: %d (expect 19) | currentText on combos: %d (expect 0)'
          % (n_current, n_text))
    if n_current != 19:
        failures.append('currentData() count changed: %d' % n_current)
    if n_text:
        failures.append('combo lookups still read displayed text')

    # 跨页对话框不得再用标签文字做状态判断
    spread = io.open(os.path.join(ROOT, 'kindlecomicconverter', 'KCC_spread_label.py'),
                     encoding='utf-8').read()
    n_label_cmp = spread.count('label2.text()')
    print('spread dialog label-text comparisons: %d (expect 0)' % n_label_cmp)
    if n_label_cmp:
        failures.append('spread dialog compares label text again')

    print()
    if failures:
        print('FAILED:')
        for f in failures:
            print('  -', f)
        return 1
    print('ALL INVARIANTS OK')
    return 0


if __name__ == '__main__':
    sys.exit(main())
