# -*- coding: utf-8 -*-
"""12.x 官方 i18n 架构的翻译覆盖率审计（取代旧 strict_audit 的源串罗列语义）。

旧机制（11.x）：apply_zh.py 原位替换，strict_audit 找源码里残留英文。
新机制（12.1.1 起）：源码保持英文，经 Qt tr()/translate() 由 .qm 运行时翻译——
源码里有英文是**正确架构**，遗漏的定义是「translate() 的源串在 .ts 中
没有对应上下文的成品译文（空译或 unfinished）」。

本脚本用 AST 提取全部 translate(ctx, src) 调用位点，与 kcc_zh_CN.ts 的
<context>/<source>/<translation> 交叉核对，报告缺失。退出码 0=全覆盖。

Usage:  <venv>\\Scripts\\python.exe tools/zh/audit_i18n_coverage.py
"""
import ast
import io
import os
import sys
import xml.etree.ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
PKG = os.path.join(ROOT, 'kindlecomicconverter')
TS = os.path.join(ROOT, 'translations', 'kcc_zh_CN.ts')

FILES = ['KCC_ui.py', 'KCC_gui.py', 'KCC_ui_editor.py']


def extract_calls(path):
    """返回 [(ctx, src, lineno), ...]"""
    src = io.open(path, encoding='utf-8').read()
    tree = ast.parse(src)
    res = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) \
                and node.func.attr == 'translate' and len(node.args) >= 2:
            a0, a1 = node.args[0], node.args[1]
            if isinstance(a0, ast.Constant) and isinstance(a0.value, str) \
                    and isinstance(a1, ast.Constant) and isinstance(a1.value, str):
                res.append((a0.value, a1.value, node.lineno))
    return res


def load_ts():
    """返回 {(ctx, src): translation}，只收成品译文。"""
    out = {}
    tree = ET.parse(TS)
    for ctx in tree.getroot().iter('context'):
        name = ctx.findtext('name')
        for msg in ctx.iter('message'):
            if msg.get('type') == 'vanished':
                continue
            src_text = msg.findtext('source')
            tr = msg.find('translation')
            if tr is None:
                continue
            if tr.get('type') == 'unfinished':
                continue
            if tr.text:
                out[(name, src_text)] = tr.text
    return out


def main():
    calls = []
    for f in FILES:
        calls.extend([(ctx, s, ln, f) for ctx, s, ln in
                      extract_calls(os.path.join(PKG, f))])
    table = load_ts()

    missing = []
    for ctx, s, ln, f in calls:
        if (ctx, s) not in table:
            missing.append((f, ln, ctx, s))

    print('translate() 调用位点: %d（%s）' % (len(calls), ', '.join(FILES)))
    print('.ts 成品译文: %d 条' % len(table))
    print('缺失: %d' % len(missing))
    if missing:
        for f, ln, ctx, s in missing[:40]:
            print('  MISS %s:%d [%s] %r' % (f, ln, ctx, s[:60]))
        out = io.open(os.path.join(HERE, 'i18n_coverage_miss.txt'), 'w',
                      encoding='utf-8')
        for f, ln, ctx, s in missing:
            out.write('%s:%d [%s] %r\n' % (f, ln, ctx, s))
        out.close()
        return 1
    print('全覆盖：所有 translate() 源串均有成品中文译文')
    return 0


if __name__ == '__main__':
    sys.exit(main())
