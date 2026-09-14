# -*- coding: utf-8 -*-
"""Inventory every user-visible string in the running UI.

A coverage aid rather than a pass/fail test: it dumps all widget text, tooltips,
combo items and placeholders, marking entries that still look like English prose.
Use it to review wording, spot untranslated text, and confirm what is
intentionally kept in English (format labels, brand names).

Output goes to .cache/widget_strings.txt (gitignored); the console prints a
summary. Runs headless via QT_QPA_PLATFORM=offscreen.
"""
import io
import os
import re
import sys

os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')
os.environ['QT_LOGGING_RULES'] = 'qt.qpa.*=false'

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, ROOT)
os.chdir(ROOT)

from PySide6.QtWidgets import (QAbstractButton, QComboBox, QDoubleSpinBox,  # noqa: E402
                               QGroupBox, QLabel, QLineEdit, QSpinBox,
                               QTabWidget, QWidget)

from kindlecomicconverter import KCC_gui  # noqa: E402

HTML = re.compile(r'<[^>]+>')
# 整串匹配的非散文词条（格式标签、技术名词）
KEEP_EXACT = {
    'JPEG/PNG/mozJpeg', 'MOBI/AZW3', 'MOBI + EPUB', 'EPUB', 'CBZ', 'PDF', 'KFX',
    'MOBI', 'Kindle', 'KOReader',
}


def is_english_prose(v):
    """Heuristic: looks like an untranslated English sentence/label."""
    plain = HTML.sub('', v).replace('&quot;', '"').replace('&amp;', '&')
    if not re.search(r'[A-Za-z]{3,}', plain):
        return False
    if any(ord(c) > 127 for c in v):
        return False
    t = plain.strip()
    if len(t) < 4 or t in KEEP_EXACT:
        return False
    # 品牌/型号/单词语条不算散文
    if len(t.split()) < 2:
        return False
    return True


def texts_of(w):
    """Return (kind, value) pairs for each user-visible string on the widget."""
    out = []
    if isinstance(w, QComboBox):
        out.append(('currentText', w.currentText()))
        out.append(('currentData', str(w.currentData())))
        out += [('item[%d]' % i, w.itemText(i)) for i in range(w.count())]
    if isinstance(w, QAbstractButton):
        out += [('text', w.text()), ('toolTip', w.toolTip())]
    if isinstance(w, (QLabel, QGroupBox)):
        out += [('text', w.text()), ('toolTip', w.toolTip())]
    if isinstance(w, QLineEdit):
        out += [('placeholder', w.placeholderText()), ('text', w.text()),
                ('toolTip', w.toolTip())]
    if isinstance(w, (QSpinBox, QDoubleSpinBox)):
        out += [('prefix', w.prefix()), ('suffix', w.suffix()),
                ('specialValueText', w.specialValueText())]
    if isinstance(w, QTabWidget):
        out += [('tab[%d]' % i, w.tabText(i)) for i in range(w.count())]
    return out


def main():
    app = KCC_gui.QApplicationMessaging(sys.argv)
    window = KCC_gui.QMainWindowKCC()
    KCC_gui.KCCGUI(app, window)
    app.processEvents()

    rows = []
    for w in window.findChildren(QWidget):
        for kind, val in texts_of(w):
            if val:
                rows.append((w.objectName(), w.__class__.__name__, kind, val))

    cache = os.path.join(ROOT, '.cache')
    os.makedirs(cache, exist_ok=True)
    dest = os.path.join(cache, 'widget_strings.txt')
    seen = set()
    english = []
    with io.open(dest, 'w', encoding='utf-8') as out:
        out.write('=== 界面可见文字清单 ===\n')
        for obj, cls, kind, val in rows:
            key = (obj, kind, val)
            if key in seen:
                continue
            seen.add(key)
            mark = 'EN?' if is_english_prose(val) else '   '
            out.write('%s %-28s %-18s %-16s %r\n' % (mark, obj, cls, kind, val[:110]))
            if mark == 'EN?':
                english.append((obj, cls, kind, val))

    print('visible strings      :', len(seen))
    print('english-prose flagged:', len(english))
    for obj, cls, kind, val in english:
        print('  EN?', obj, cls, kind, repr(val[:90]))
    print('full listing written to', dest)
    return 0


if __name__ == '__main__':
    sys.exit(main())
