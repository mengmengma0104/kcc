# -*- coding: utf-8 -*-
"""修复 12.1.1 固定分辨率设备项：zhDeviceNames 缺 FIXED_RES_STRINGS 键导致 KeyError。

12.1.1 上游把 image.ProfileData.FIXED_RESOLUTIONS 生成的分辨率字符串
（如 '2400x3200'，f-string 动态生成，源码中无字面量）展开进 profilesGUI，
作为「固定分辨率」设备项。显示名即分辨率本身（纯数字，无需翻译），
但 DEVICE_NAMES 生成脚本从 profilesGUI 的 AST 字面量提取键，看不到
展开项，导致映射缺键。本脚本：

1. display_names.py 的 DEVICE_NAMES 补 7 个固定分辨率键（映射为自身）
2. verify_invariants.py 新增不变量：DEVICE_NAMES 必须覆盖全部固定分辨率键
3. verify_keys.py 的 EXPECTED_PROFILES 同步为 verify_invariants.py 的现值
   （旧文件还停留在 11.3.2 的 45 键清单，避免留陷阱）
"""
import ast
import io
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))

# 与 image.py FIXED_RESOLUTIONS（reverse 后）一致；上游若改动，不变量会报警
FIXED_RES = ['2400x3200', '1860x2480', '1650x2200', '1536x2048',
             '1404x1872', '1264x1680', '1072x1448']


def patch_display_names():
    p = os.path.join(HERE, 'display_names.py')
    src = io.open(p, encoding='utf-8').read()
    m = re.search(r'DEVICE_NAMES = \{(.*?)\n\}\n', src, re.S)
    if not m:
        raise SystemExit('DEVICE_NAMES 块定位失败')
    block = m.group(1)
    have = set(re.findall(r"'([^']+)':", block))
    missing = [k for k in FIXED_RES if k not in have]
    if not missing:
        print('display_names.py: 固定分辨率键已齐，跳过')
        return
    entries = ''.join("    '%s': '%s',  # 固定分辨率设备项（image.py 动态生成）\n" % (k, k)
                      for k in FIXED_RES)
    new_block = block.rstrip('\n') + '\n' + entries
    src = src[:m.start(1)] + new_block + src[m.end(1):]
    io.open(p, 'w', encoding='utf-8', newline='\n').write(src)
    print('display_names.py: 补入 %d 个固定分辨率键 %s' % (len(missing), missing))


def patch_verify_invariants():
    p = os.path.join(HERE, 'verify_invariants.py')
    src = io.open(p, encoding='utf-8').read()
    if '固定分辨率设备项' in src:
        print('verify_invariants.py: 已有固定分辨率不变量，跳过')
        return
    anchor = "    # 跨页对话框不得再用标签文字做状态判断"
    add = (
        "    # 固定分辨率设备项（12.1.1 起 image.py 动态生成）必须有显示名映射\n"
        "    dn_src = io.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'display_names.py'), encoding='utf-8').read()\n"
        "    for res in ['2400x3200', '1860x2480', '1650x2200', '1536x2048',\n"
        "                '1404x1872', '1264x1680', '1072x1448']:\n"
        "        if (\"'%s':\" % res) not in dn_src:\n"
        "            failures.append('DEVICE_NAMES 缺固定分辨率键 %s' % res)\n"
        "    print('fixed-res display keys: 7 项检查完成')\n\n"
    )
    if anchor not in src:
        raise SystemExit('verify_invariants.py 插入锚点未找到')
    src = src.replace(anchor, add + anchor, 1)
    io.open(p, 'w', encoding='utf-8', newline='\n').write(src)
    print('verify_invariants.py: 新增固定分辨率覆盖不变量')


def reinject_zhdevnames():
    """KCC_gui.py 里的 zhDeviceNames 是注入时的字面量快照——
    display_names.py 改动后必须重新注入才生效。"""
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        'display_names', os.path.join(HERE, 'display_names.py'))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    device_names = mod.DEVICE_NAMES

    p = os.path.join(ROOT, 'kindlecomicconverter', 'KCC_gui.py')
    src = io.open(p, encoding='utf-8').read()
    m = re.search(r'        zhDeviceNames = \{.*?\n        \}\n', src, re.S)
    if not m:
        raise SystemExit('KCC_gui.py zhDeviceNames 块定位失败')
    lines = ['        zhDeviceNames = {\n']
    for k, v in device_names.items():
        lines.append('            %r: %r,\n' % (k, v))
    lines.append('        }\n')
    src = src[:m.start()] + ''.join(lines) + src[m.end():]
    io.open(p, 'w', encoding='utf-8', newline='\n').write(src)
    print('KCC_gui.py: zhDeviceNames 重新注入（%d 键）' % len(device_names))


if __name__ == '__main__':
    patch_display_names()
    patch_verify_invariants()
    reinject_zhdevnames()
    print('完成')
