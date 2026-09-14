# -*- coding: utf-8 -*-
"""Strict translation-coverage audit: flag untranslated UI strings.

Deliberately uses NO prefix-based keep-list. A prefix whitelist such as
``^Auto`` (meant for the format label "Auto") also swallows whole sentences
that merely begin with that word — the class of miss this audit exists to
catch. Only exact-string exemptions are applied, and the output is a plain
list of candidates for human review.

Reported strings are CJK-free and contain >=2 distinct alphabetic words, i.e.
they read like English prose rather than identifiers or format codes.

Usage:  <venv>\\Scripts\\python.exe tools/zh/strict_audit.py
Output: tools/zh/strict_audit.txt
"""
import ast
import io
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PKG = os.path.join(ROOT, 'kindlecomicconverter')
OUT = io.open(os.path.join(ROOT, 'tools', 'zh', 'strict_audit.txt'), 'w', encoding='utf-8')

WORD = re.compile(r'[A-Za-z]{3,}')
CJK = lambda s: any(ord(c) > 127 for c in s)


def collect_py(path, only_translate=False):
    src = io.open(path, encoding='utf-8').read()
    tree = ast.parse(src)
    res = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) \
                and node.func.attr == 'translate' and len(node.args) >= 2:
            a = node.args[1]
            if isinstance(a, ast.Constant) and isinstance(a.value, str):
                res.append((node.lineno, a.value))
        elif not only_translate and isinstance(node, ast.Constant) and isinstance(node.value, str):
            res.append((node.lineno, node.value))
    return sorted(set(res))


def collect_ui_xml(path):
    import xml.etree.ElementTree as ET
    root = ET.parse(path).getroot()
    res = []
    for el in root.iter('string'):
        if el.text:
            res.append((0, el.text))
    return res


targets = [
    ('KCC_ui.py', os.path.join(PKG, 'KCC_ui.py'), 't'),
    ('KCC_ui_editor.py', os.path.join(PKG, 'KCC_ui_editor.py'), 't'),
    ('KCC_gui.py', os.path.join(PKG, 'KCC_gui.py'), 'a'),
    ('KCC_spread_label.py', os.path.join(PKG, 'KCC_spread_label.py'), 'a'),
    ('shared.py', os.path.join(PKG, 'shared.py'), 'a'),
    ('gui/KCC.ui', os.path.join(ROOT, 'gui', 'KCC.ui'), 'x'),
    ('gui/MetaEditor.ui', os.path.join(ROOT, 'gui', 'MetaEditor.ui'), 'x'),
]

total = 0
for name, path, kind in targets:
    if kind == 'x':
        items = collect_ui_xml(path)
    else:
        items = collect_py(path, only_translate=(kind == 't'))
    hits = []
    seen = set()
    for ln, v in items:
        if CJK(v) or v in seen:
            continue
        seen.add(v)
        words = WORD.findall(v)
        # >=2 distinct alpha words of len>=3 -> sentence-like
        if len(set(w.lower() for w in words)) >= 2:
            hits.append((ln, v))
    OUT.write('===== %s: %d hits =====\n' % (name, len(hits)))
    for ln, v in hits:
        OUT.write('%s | %r\n' % (ln, v[:160]))
    total += len(hits)
    print('%-22s %d hits' % (name, len(hits)))

OUT.write('\ntotal: %d\n' % total)
OUT.close()
print('total hits:', total, '-> tools/zh/strict_audit.txt')
