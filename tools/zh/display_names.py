# -*- coding: utf-8 -*-
"""显示名映射：下拉框的中文显示文字 ↔ 内部英文键值。

键是 KCC 内部使用的英文标识（profiles / formats 字典的键），值是界面上
呈现给用户的中文名称。设备型号名按惯例保留英文原文，仅彩色机型追加
「（彩色）」标注以便区分；通用词条（如 Other）译为中文。

数据从上游 12.1.1 源码的 profiles/formats 键集生成（由综合修复脚本写入）。
"""

DEVICE_NAMES = {
    'Kindle Oasis 9/10': 'Kindle Oasis 9/10',
    'Kindle 8/10': 'Kindle 8/10',
    'Kindle Oasis 8': 'Kindle Oasis 8',
    'Kindle Voyage': 'Kindle Voyage',
    'Kindle 1860x1920': 'Kindle 1860x1920',
    'Kindle 1920x1920': 'Kindle 1920x1920',
    'Kindle 1240x1860': 'Kindle 1240x1860',
    'Kindle 1324x1986': 'Kindle 1324x1986',
    'Kindle Scribe 1/2': 'Kindle Scribe 1/2',
    'Kindle Scribe 3': 'Kindle Scribe 3',
    'Kindle Scribe Colorsoft': 'Kindle Scribe Colorsoft（彩色）',
    'Kindle 11/2026': 'Kindle 11/2026',
    'Kindle Paperwhite 11': 'Kindle Paperwhite 11',
    'Kindle Paperwhite 12/2026': 'Kindle Paperwhite 12/2026',
    'Kindle Colorsoft': 'Kindle Colorsoft（彩色）',
    'Kindle Paperwhite 7/10': 'Kindle Paperwhite 7/10',
    'Kindle Paperwhite 5/6': 'Kindle Paperwhite 5/6',
    'Kindle 4/5/7': 'Kindle 4/5/7',
    'Kindle DX': 'Kindle DX',
    'Kobo Mini/Touch': 'Kobo Mini/Touch',
    'Kobo Glo': 'Kobo Glo',
    'Kobo Glo HD': 'Kobo Glo HD',
    'Kobo Aura': 'Kobo Aura',
    'Kobo Aura HD': 'Kobo Aura HD',
    'Kobo Aura H2O': 'Kobo Aura H2O',
    'Kobo Aura ONE': 'Kobo Aura ONE',
    'Kobo Clara HD': 'Kobo Clara HD',
    'Kobo Libra H2O': 'Kobo Libra H2O',
    'Kobo Forma': 'Kobo Forma',
    'Kindle 1': 'Kindle 1',
    'Kindle 2': 'Kindle 2',
    'Kindle Keyboard': 'Kindle Keyboard',
    'Kindle Touch': 'Kindle Touch',
    'Kobo Nia': 'Kobo Nia',
    'Kobo Clara 2E/BW': 'Kobo Clara 2E/BW',
    'Kobo Clara Colour': 'Kobo Clara Colour（彩色）',
    'Kobo Libra 2': 'Kobo Libra 2',
    'Kobo Libra Colour': 'Kobo Libra Colour（彩色）',
    'Kobo Sage': 'Kobo Sage',
    'Kobo Elipsa': 'Kobo Elipsa',
    'reMarkable 1/2/Pure': 'reMarkable 1/2/Pure',
    'reMarkable Paper Pro': 'reMarkable Paper Pro',
    'reMarkable Paper Pro Move': 'reMarkable Paper Pro Move',
    'Other': '其他设备（自定义分辨率）',
    '2400x3200': '2400x3200',  # 固定分辨率设备项（image.py 动态生成）
    '1860x2480': '1860x2480',  # 固定分辨率设备项（image.py 动态生成）
    '1650x2200': '1650x2200',  # 固定分辨率设备项（image.py 动态生成）
    '1536x2048': '1536x2048',  # 固定分辨率设备项（image.py 动态生成）
    '1404x1872': '1404x1872',  # 固定分辨率设备项（image.py 动态生成）
    '1264x1680': '1264x1680',  # 固定分辨率设备项（image.py 动态生成）
    '1072x1448': '1072x1448',  # 固定分辨率设备项（image.py 动态生成）

}

FORMAT_NAMES = {
    'MOBI/AZW3': 'MOBI/AZW3',
    'EPUB': 'EPUB',
    'CBZ': 'CBZ',
    'Preview/Folder of images': 'Preview/Folder of images',
    'PDF': 'PDF',
    'PDF (200MB limit)': 'PDF (200MB limit)',
    'KFX (Send to Kindle EPUB)': 'KFX (Send to Kindle EPUB)',
    'MOBI + EPUB': 'MOBI + EPUB',
    'EPUB (200MB limit)': 'EPUB (200MB limit)',
    'MOBI + EPUB (200MB limit)': 'MOBI + EPUB (200MB limit)',
}
