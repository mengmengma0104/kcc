# -*- coding: utf-8 -*-
"""Offscreen regression test for the localized UI.

Three checks, all headless (QT_QPA_PLATFORM=offscreen):
  1. Combo coverage — every device and format entry is driven through the real
     code path (changeDevice/changeFormat + get_options) to prove the
     display-text/userData split resolves without KeyError.
  2. Tooltip assertions — user-visible tooltips and labels that are easy to miss
     (long multi-line ones especially) must be Chinese, not English.
  3. Strict English scan — walk the live widget tree and report any remaining
     English prose. Uses an exact-match keep-list only; prefix matching would
     hide whole sentences that merely start with a kept word.
"""
import os
import re
import sys
import traceback

os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')
os.environ['QT_LOGGING_RULES'] = 'qt.qpa.*=false'

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, ROOT)
os.chdir(ROOT)

from PySide6.QtWidgets import (QAbstractButton, QComboBox, QGroupBox,  # noqa: E402
                               QLabel, QWidget)

from kindlecomicconverter import KCC_gui  # noqa: E402

# 刻意保留英文的非散文字符串（格式标签、技术名词）——必须整串匹配
KEEP_EXACT = {'JPEG/PNG/mozJpeg', 'MOBI/AZW3', 'MOBI + EPUB', 'EPUB', 'CBZ', 'PDF', 'KFX'}
BRAND = re.compile(r'^(Kindle|Kobo|reMarkable|MOBI|EPUB|CBZ|PDF|KFX|FOLDER|RAR)'
                   r'([ 0-9/xa-zA-Z+()（）：:．.·-]*?)$')
HTML = re.compile(r'<[^>]+>')

# 易漏的界面文字：抽查这些必须是中文
TOOLTIP_PROBES = [
    ('wallpaperBox', '壁纸模式'),
    ('legacyExtractBox', '旧版提取方式'),
    ('jpegQualityBox', 'JPEG'),
    ('onePageLandscapeBox', '横向'),
]


def is_english_prose(v):
    """True if the string looks like untranslated English prose (not a code/brand)."""
    plain = HTML.sub('', v).replace('&quot;', '"').replace('&amp;', '&')
    words = re.findall(r'[A-Za-z]{3,}', plain)
    if len(set(w.lower() for w in words)) < 2:
        return False
    if any(ord(c) > 127 for c in v):
        return False
    t = v.strip()
    if t in KEEP_EXACT:
        return False
    if BRAND.match(t) and len(words) <= 4 and not re.search(r'[.!?]', t):
        return False
    return True


def widget_strings(window):
    """Yield (objectName, className, text) for every user-visible string."""
    for w in window.findChildren(QWidget):
        vals = []
        if isinstance(w, QAbstractButton):
            vals += [w.text(), w.toolTip()]
        if isinstance(w, (QLabel, QGroupBox)):
            vals += [w.text(), w.toolTip()]
        if isinstance(w, QComboBox):
            vals += [w.toolTip()] + [w.itemText(i) for i in range(w.count())]
        for v in vals:
            if v:
                yield w.objectName(), w.__class__.__name__, v


def main():
    app = KCC_gui.QApplicationMessaging(sys.argv)
    window = KCC_gui.QMainWindowKCC()
    gui = KCC_gui.KCCGUI(app, window)

    device, fmt = gui.deviceBox, gui.formatBox
    errors = []
    brand_en = []
    device_ok = format_ok = 0

    # ---- 1a. devices ----
    for i in range(device.count()):
        data = device.itemData(i)
        if data is None:                      # separator row
            continue
        text = device.itemText(i)
        if data not in gui.profiles:
            errors.append(f'device[{i}] userData {data!r} not a profiles key')
            continue
        device.setCurrentIndex(i)
        try:
            gui.changeDevice()
            opts, _ = KCC_gui.get_options()
        except Exception as e:
            errors.append(f'device[{i}] {data!r} ({text!r}) -> {type(e).__name__}: {e}')
            traceback.print_exc()
            continue
        label = gui.profiles[data]['Label']
        if opts.profile != label:
            errors.append(f'device[{i}] {data!r}: profile {opts.profile!r} != {label!r}')
            continue
        # 品牌/型号名保持英文是设计选择；这里只统计，不算错误
        if not any(ord(c) > 127 for c in text):
            brand_en.append(text)
        device_ok += 1

    # ---- 1b. formats ----
    for i in range(fmt.count()):
        data = fmt.itemData(i)
        if data is None:
            continue
        text = fmt.itemText(i)
        if data not in gui.formats:
            errors.append(f'format[{i}] userData {data!r} not a formats key')
            continue
        fmt.setCurrentIndex(i)
        try:
            gui.changeFormat(i)
            opts, _ = KCC_gui.get_options()
        except Exception as e:
            errors.append(f'format[{i}] {data!r} ({text!r}) -> {type(e).__name__}: {e}')
            traceback.print_exc()
            continue
        expected = gui.formats[data]['format']
        if opts.format != expected:
            errors.append(f'format[{i}] {data!r}: format {opts.format!r} != {expected!r}')
            continue
        format_ok += 1

    # ---- 2. tooltip probes ----
    print('--- 工具提示抽查（应为中文）---')
    for obj_name, hint in TOOLTIP_PROBES:
        w = getattr(gui, obj_name, None)
        if w is None:
            errors.append(f'tooltip probe: widget {obj_name} not found')
            continue
        tip = w.toolTip() or ''
        is_cn = any(ord(c) > 127 for c in tip)
        print('  %-24s %s  %s' % (obj_name, '中文' if is_cn else '英文!', tip[:60]))
        if not is_cn:
            errors.append(f'{obj_name} tooltip still English: {tip[:80]!r}')

    # ---- 3. strict English scan ----
    seen = set()
    leftovers = []
    for obj, cls, v in widget_strings(window):
        if is_english_prose(v) and v not in seen:
            seen.add(v)
            leftovers.append((obj, cls, v))
    print()
    print('--- 严格英文扫描（无前缀白名单）---')
    print('  残留英文散文:', len(leftovers))
    for obj, cls, v in leftovers:
        print('   EN?', obj, cls, repr(v[:90]))

    print()
    print(f'devices exercised OK : {device_ok}')
    print(f'formats exercised OK : {format_ok}')
    print(f'errors               : {len(errors)}')
    for e in errors:
        print('  ERROR:', e)
    print(f'brand names kept EN  : {len(brand_en)}')
    print()
    print('window title :', window.windowTitle())
    print('convert btn  :', gui.convertButton.text())
    print('device text  :', device.itemText(0))
    print('format text  :', fmt.itemText(0))

    return 1 if (errors or leftovers) else 0


if __name__ == '__main__':
    sys.exit(main())
