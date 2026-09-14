# -*- coding: utf-8 -*-
"""Apply the Chinese translation table to KCC Python sources and .ui files.

Three layers of replacement:
  1. Python string literals — AST-driven exact span replacement, so only the
     literal payload changes and surrounding code/formatting is untouched.
  2. f-string fragments — verbatim source-snippet substitution for literals that
     contain interpolation (their placeholders must stay live, so they cannot be
     looked up by whole-string value). Snippets come from translations.FSTRING_FRAGMENTS.
  3. Qt .ui files — ElementTree rewrite of <string> element text.

Idempotent: re-running over already-translated sources reports 0 replacements.
"""
import ast
import io
import os
import sys
import xml.etree.ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
# 项目根：默认按脚本位置推导（tools/zh/ 的上两级）；
# 设置 KCC_REPLAY_ROOT 可指向其他源码树（用于从原始源码重放验证）。
ROOT = os.environ.get('KCC_REPLAY_ROOT') or os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)

from translations import (UI, MESSAGES, FSTRING_FRAGMENTS,  # noqa: E402
                          HARDENING_COMBO, SPREAD_DIALOG_REPLACEMENTS,
                          HARDENING_TARGETS)
from display_names import DEVICE_NAMES, FORMAT_NAMES  # noqa: E402

TABLE = {}
TABLE.update(UI)
TABLE.update(MESSAGES)

# 含插值的源码文件（f-string 片段所在）
FSTRING_TARGETS = ['kindlecomicconverter/KCC_gui.py']


def escape_literal(value):
    """Render a Python string literal the way the source files do (u"..." / "...")."""
    out = value.replace('\\', '\\\\').replace('"', '\\"')
    out = out.replace('\n', '\\n').replace('\r', '\\r').replace('\t', '\\t')
    return out


def apply_python(path):
    src = io.open(path, encoding='utf-8').read()
    tree = ast.parse(src)
    lines = src.splitlines(keepends=True)
    # byte/char offsets per line start
    offsets = []
    pos = 0
    for line in lines:
        offsets.append(pos)
        pos += len(line)

    edits = []          # (start, end, replacement)
    matched = {}        # translation -> count
    for node in ast.walk(tree):
        if not (isinstance(node, ast.Constant) and isinstance(node.value, str)):
            continue
        if node.value not in TABLE:
            continue
        new = TABLE[node.value]
        if new == node.value:
            continue
        start = offsets[node.lineno - 1] + node.col_offset
        end = offsets[node.end_lineno - 1] + node.end_col_offset
        original = src[start:end]
        prefix = ''
        if original[:1] in ('u', 'U', 'f', 'F', 'r', 'R', 'b', 'B'):
            prefix = original[0]
        if 'f' in prefix.lower():
            # never rewrite f-strings: placeholders must stay live
            continue
        body = src[start + len(prefix):end]
        quote = body[:3] if body[:3] in ('"""', "'''") else body[:1]
        if quote not in ('"', "'", '"""', "'''"):
            continue
        edits.append((start, end, prefix + quote + escape_literal(new) + quote))
        matched[node.value] = matched.get(node.value, 0) + 1

    if not edits:
        return 0, []

    edits.sort(key=lambda e: e[0], reverse=True)
    out = src
    for start, end, rep in edits:
        out = out[:start] + rep + out[end:]

    io.open(path, 'w', encoding='utf-8', newline='').write(out)
    return len(edits), sorted(matched.keys())


def apply_ui(path):
    tree = ET.parse(path)
    root = tree.getroot()
    count = 0
    for string_el in root.iter('string'):
        if string_el.text and string_el.text in TABLE:
            new = TABLE[string_el.text]
            if new != string_el.text:
                string_el.text = new
                count += 1
        # <string notr="true"> must never be translated
    if count:
        tree.write(path, encoding='utf-8', xml_declaration=True)
    return count


def render_dict(name, mapping, indent=8):
    """把映射渲染成源码中的字典字面量（整体缩进 indent 个空格，双引号风格）。"""
    pad = ' ' * indent

    def q(s):
        # 与工作树风格一致：双引号，内部双引号转义
        return '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'

    lines = [pad + name + ' = {']
    for k, v in mapping.items():
        lines.append('%s%s: %s,' % (pad + '    ', q(k), q(v)))
    lines.append(pad + '}')
    return '\n'.join(lines)


def apply_combo_display_names(path):
    """注入中文显示名映射，并把 addItem 改为三参数形式（显示中文 + userData 英文键）。"""
    src = io.open(path, encoding='utf-8').read()
    changed = 0

    # 锚点必须唯一：`self.modeChange(1)` 在源码中出现两次，
    # 只有 __init__ 中紧邻 togglecroppingBox 定义的那一处才是组合框初始化位置。
    anchor = ('        self.modeChange(1)\n'
              '        for profile in profilesGUI:')
    if anchor in src and 'zhDeviceNames = {' not in src:
        block = (
            '        # 中文界面文字与内部英文键值分离：显示中文，userData 保存英文键，\n'
            '        # 逻辑查找一律走 currentData()，避免界面翻译影响 profiles/formats 查表。\n'
            + render_dict('zhDeviceNames', DEVICE_NAMES) + '\n'
            + render_dict('zhFormatNames', FORMAT_NAMES) + '\n'
        )
        src = src.replace(anchor, '        self.modeChange(1)\n' + block
                          + '        for profile in profilesGUI:', 1)
        changed += 1

    additem_pairs = [
        ('GUI.deviceBox.addItem(self.icons.deviceOther, profile)',
         'GUI.deviceBox.addItem(self.icons.deviceOther, zhDeviceNames[profile], profile)'),
        ('GUI.deviceBox.addItem(self.icons.deviceRmk, profile)',
         'GUI.deviceBox.addItem(self.icons.deviceRmk, zhDeviceNames[profile], profile)'),
        ('GUI.deviceBox.addItem(self.icons.deviceKobo, profile)',
         'GUI.deviceBox.addItem(self.icons.deviceKobo, zhDeviceNames[profile], profile)'),
        ('GUI.deviceBox.addItem(self.icons.deviceKindle, profile)',
         'GUI.deviceBox.addItem(self.icons.deviceKindle, zhDeviceNames[profile], profile)'),
        ("GUI.formatBox.addItem(getattr(self.icons, self.formats[f]['icon'] + 'Format'), f)",
         "GUI.formatBox.addItem(getattr(self.icons, self.formats[f]['icon'] + 'Format'),"
         " zhFormatNames[f], f)"),
    ]
    for old, new in additem_pairs:
        n = src.count(old)
        if n:
            src = src.replace(old, new)
            changed += n

    # 元数据编辑器的字段标题（显示在批量编辑提示框中）
    field_pairs = [
        ("(self.seriesLine, 'Series',", "(self.seriesLine, '系列',"),
        ("(self.writerLine, 'Writer',", "(self.writerLine, '编剧',"),
        ("(self.pencillerLine, 'Penciller',", "(self.pencillerLine, '作画',"),
        ("(self.inkerLine, 'Inker',", "(self.inkerLine, '墨线',"),
        ("(self.coloristLine, 'Colorist',", "(self.coloristLine, '上色',"),
    ]
    for old, new in field_pairs:
        n = src.count(old)
        if n:
            src = src.replace(old, new)
            changed += n

    if changed:
        io.open(path, 'w', encoding='utf-8', newline='').write(src)
    print('   combo display names + field titles:', changed)
    return changed


def apply_fstring_fragments(path):
    """在含插值的源码中做整片段替换（占位符保持活跃）。"""
    src = io.open(path, encoding='utf-8').read()
    changed = 0
    for old, new in FSTRING_FRAGMENTS.items():
        n = src.count(old)
        if n:
            src = src.replace(old, new)
            changed += n
    if changed:
        io.open(path, 'w', encoding='utf-8', newline='').write(src)
    return changed


def apply_hardening(path, kind):
    """应用代码加固（幂等：已加固的源码中不存在待替换的旧写法）。"""
    src = io.open(path, encoding='utf-8').read()
    changed = 0
    if kind == 'combo':
        for old, new in HARDENING_COMBO.items():
            n = src.count(old)
            if n:
                src = src.replace(old, new)
                changed += n
        print('   combo lookups hardened:', changed)
    elif kind == 'spread':
        for old, new in SPREAD_DIALOG_REPLACEMENTS:
            n = src.count(old)
            if n:
                src = src.replace(old, new, 1)
                changed += 1
        print('   spread-dialog replacements:', changed)
    if changed:
        io.open(path, 'w', encoding='utf-8', newline='').write(src)
    return changed


def main():
    targets_py = [
        os.path.join(ROOT, 'kindlecomicconverter', 'KCC_gui.py'),
        os.path.join(ROOT, 'kindlecomicconverter', 'KCC_ui.py'),
        os.path.join(ROOT, 'kindlecomicconverter', 'KCC_ui_editor.py'),
        os.path.join(ROOT, 'kindlecomicconverter', 'KCC_spread_label.py'),
        os.path.join(ROOT, 'kindlecomicconverter', 'shared.py'),
    ]
    targets_ui = [
        os.path.join(ROOT, 'gui', 'KCC.ui'),
        os.path.join(ROOT, 'gui', 'MetaEditor.ui'),
    ]

    total = 0
    used = set()
    missing = []
    # 加固必须先于翻译：它针对上游的英文原文写法做结构替换
    for kind, rels in HARDENING_TARGETS.items():
        for rel in rels:
            p = os.path.join(ROOT, rel)
            if not os.path.exists(p):
                missing.append(rel)
                continue
            print('hardening %s (%s)' % (os.path.basename(p), kind))
            total += apply_hardening(p, kind)
    for rel in FSTRING_TARGETS:
        p = os.path.join(ROOT, rel)
        if os.path.exists(p):
            n = apply_combo_display_names(p)
            total += n
            n = apply_fstring_fragments(p)
            total += n
            print(f'{os.path.basename(p):24s} f-string fragments {n}')
        else:
            missing.append(rel)
    for p in targets_py + targets_ui:
        if not os.path.exists(p):
            missing.append(os.path.relpath(p, ROOT))
            continue
        if p in targets_py:
            n, keys = apply_python(p)
            used.update(keys)
        else:
            n = apply_ui(p)
        total += n
        print(f'{os.path.basename(p):24s} replaced {n}')

    # 目标文件缺失通常意味着 ROOT 指错了位置（例如重放时路径未对齐），
    # 静默跳过会让调用方误以为翻译成功，因此必须显式报错。
    if missing:
        print()
        print('ERROR: 以下目标文件未找到，ROOT 可能不正确: %s' % ROOT)
        for rel in missing:
            print('   MISSING:', rel)
        return 2

    print('total replacements:', total)
    unused = sorted(k for k in TABLE if k not in used)
    print('table entries never matched:', len(unused))
    for k in unused[:40]:
        print('   UNUSED:', repr(k)[:110])
    return 0


if __name__ == '__main__':
    sys.exit(main())
