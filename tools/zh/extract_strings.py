# -*- coding: utf-8 -*-
"""Extract user-visible string candidates from KCC source for translation."""
import ast
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PKG = os.path.join(ROOT, 'kindlecomicconverter')

# strings never worth translating: encodings, modes, format codes, internal sentinels
SKIP_EXACT = {
    'utf-8', 'utf8', 'w', 'r', 'rb', 'wb', 'a', 'ab', 'x', 'rt', 'wt', 'b', 't',
    'ascii', 'latin-1', 'cp437', 'latin_1', 'UTF-8',
    'MOBI', 'EPUB', 'CBZ', 'PDF', 'KFX', 'FOLDER', 'AUTO', 'Auto', 'OTHER',
    'documents', 'system', 'thumbnails', 'ARISE', 'Separator', 'Other',
    'Amazon kindlegen', 'kindlegen', '7z', '7zz', 'tar', 'bsdtar', 'unar', 'unrar',
    'ComicInfo.xml', 'job.json', 'defaulttitle', 'defaultauthor',
    'ciromattia', 'kcc10', 'kcc', 'KCC', 'kcc10',
    '0x0', 'kcc10', 'KCC-', 'CBR', 'RAR', '7Z', 'ZIP', 'ZIP ', 'jpg', 'jpeg',
    'png', 'webp', 'gif', 'mobi', 'epub', 'pdf', 'cbz', 'kepub.epub',
    'en-US', 'en', 'true', 'false', 'title', 'author', 'language',
    'PVOptions', 'ForceExpert', 'DefaultFormat', 'DefaultUpscale', 'ForceColor',
    'Label', 'icon', 'format', 'Series', 'Volume', 'Number', 'Title', 'Writers',
    'Pencillers', 'Inkers', 'Colorists', 'Cover', 'CoverArtist', 'Publisher',
    'Imprint', 'Genre', 'Web', 'PageCount', 'Summary', 'Year', 'Month', 'Day',
    'Volume', 'ISBN', 'Notes', 'ScanInformation', 'BlackAndWhite',
    'Manga', 'Characters', 'Teams', 'Locations', 'StoryArc', 'SeriesGroup',
    'AlternateSeries', 'AlternateNumber', 'AlternateCount', 'Count',
    'Day', 'Month', 'Year', 'CommunityRating', 'Review', 'GTIN',
}

# substrings indicating non-UI / machine strings
SKIP_IF_CONTAINS = (
    '://', 'file://', 'http', '.png', '.jpg', '.ico', '.qrc', '.xml', '.json',
    '%LOCALAPPDATA%', '%UserProfile%', 'Program Files', '$', '\\', '/',
    'QFont', 'QLabel', 'QLayout', 'Qt::', 'PySide', 'python', 'pip ',
)

HEXCOLOR = re.compile(r'^#[0-9a-fA-F]{3,8}$')
HAS_LETTER = re.compile(r'[A-Za-z]')
# sentences / UI labels: must contain a letter and either a space or end punctuation
LOOKS_UI = re.compile(r'[A-Za-z].*(\s|[:.!?]$)')


def should_skip(s):
    if not s or len(s) < 2:
        return True
    if s in SKIP_EXACT:
        return True
    if HEXCOLOR.match(s):
        return True
    if not HAS_LETTER.search(s):
        return True
    # drop pure identifiers / codes / filenames
    if re.match(r'^[A-Za-z0-9_\-+/.:]*$', s) and not LOOKS_UI.search(s):
        return True
    lowered = s.lower()
    if any(tok.lower() in lowered for tok in SKIP_IF_CONTAINS):
        # allow strings that are clearly prose even if they contain '/'
        if not (' ' in s and LOOKS_UI.search(s)):
            return True
    if s.count('\\') > 1:
        return True
    return False


def walk_file(path):
    src = io.open(path, encoding='utf-8').read()
    tree = ast.parse(src)
    out = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            if should_skip(node.value):
                continue
            out.append({'line': getattr(node, 'lineno', 0), 'text': node.value})
    out.sort(key=lambda d: d['line'])
    return out, src


def extract_qt_translate(path):
    """Pull the u"..." payload out of QCoreApplication.translate(...) calls."""
    src = io.open(path, encoding='utf-8').read()
    tree = ast.parse(src)
    out = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) \
                and node.func.attr == 'translate' and len(node.args) >= 2:
            arg = node.args[1]
            if isinstance(arg, ast.Constant) and isinstance(arg.value, str):
                out.append({'line': node.lineno, 'text': arg.value})
    out.sort(key=lambda d: d['line'])
    return out


def main():
    result = {}
    for name in ['KCC_gui.py', 'KCC_spread_label.py', 'shared.py', 'startup.py',
                 'comic2ebook.py', 'metadata.py', 'comic2panel.py']:
        p = os.path.join(PKG, name)
        if not os.path.exists(p):
            continue
        items, _ = walk_file(p)
        result[name] = items
        print(f'{name}: {len(items)} candidates')
    for name in ['KCC_ui.py', 'KCC_ui_editor.py']:
        p = os.path.join(PKG, name)
        items = extract_qt_translate(p)
        result[name] = items
        print(f'{name}: {len(items)} qt-translate strings')

    cache = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
        os.path.abspath(__file__)))), '.cache')
    os.makedirs(cache, exist_ok=True)
    outp = os.path.join(cache, 'strings_raw.json')
    with io.open(outp, 'w', encoding='utf-8') as fh:
        json.dump(result, fh, ensure_ascii=False, indent=1)
    print('wrote', outp)


if __name__ == '__main__':
    main()
