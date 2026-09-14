# -*- coding: utf-8 -*-
"""显示名映射：下拉框的中文显示文字 ↔ 内部英文键值。

键是 KCC 内部使用的英文标识（profiles / formats 字典的键），值是界面上
呈现给用户的中文名称。设备型号名按惯例保留英文原文，仅彩色机型追加
「（彩色）」标注以便区分；通用词条（如 Other）译为中文。

这些映射由 apply_zh.py 以字面量形式注入 KCC_gui.py，与 addItem 的
第三参数（userData）配合，使逻辑查找始终基于英文键。
"""

DEVICE_NAMES = {
    "Kindle Scribe Colorsoft": "Kindle Scribe Colorsoft（彩色）",
    "Kindle Scribe 3": "Kindle Scribe 3",
    "Kindle Colorsoft": "Kindle Colorsoft（彩色）",
    "Kindle Paperwhite 12": "Kindle Paperwhite 12",
    "Kindle Scribe 1/2": "Kindle Scribe 1/2",
    "Kindle Paperwhite 11": "Kindle Paperwhite 11",
    "Kindle 11": "Kindle 11",
    "Kindle Oasis 9/10": "Kindle Oasis 9/10",
    "Kobo Clara 2E": "Kobo Clara 2E",
    "Kobo Clara Colour": "Kobo Clara Colour（彩色）",
    "Kobo Sage": "Kobo Sage",
    "Kobo Libra 2": "Kobo Libra 2",
    "Kobo Libra Colour": "Kobo Libra Colour（彩色）",
    "Kobo Elipsa": "Kobo Elipsa",
    "Kobo Nia": "Kobo Nia",
    "reMarkable 1": "reMarkable 1",
    "reMarkable 2": "reMarkable 2",
    "reMarkable Paper Pro": "reMarkable Paper Pro",
    "reMarkable Paper Pro Move": "reMarkable Paper Pro Move",
    "Other": "其他设备（自定义分辨率）",
    "Kindle 1324x1986": "Kindle 1324x1986",
    "Kindle 1920x1920": "Kindle 1920x1920",
    "Kindle 1860x1920": "Kindle 1860x1920",
    "Kindle 1240x1860": "Kindle 1240x1860",
    "Kindle 8/10": "Kindle 8/10",
    "Kindle Oasis 8": "Kindle Oasis 8",
    "Kindle Paperwhite 7/10": "Kindle Paperwhite 7/10",
    "Kindle Voyage": "Kindle Voyage",
    "Kindle Paperwhite 5/6": "Kindle Paperwhite 5/6",
    "Kindle 4/5/7": "Kindle 4/5/7",
    "Kindle Touch": "Kindle Touch",
    "Kindle Keyboard": "Kindle Keyboard",
    "Kindle DX": "Kindle DX",
    "Kindle 2": "Kindle 2",
    "Kindle 1": "Kindle 1",
    "Kobo Aura": "Kobo Aura",
    "Kobo Aura ONE": "Kobo Aura ONE",
    "Kobo Aura H2O": "Kobo Aura H2O",
    "Kobo Aura HD": "Kobo Aura HD",
    "Kobo Clara HD": "Kobo Clara HD",
    "Kobo Forma": "Kobo Forma",
    "Kobo Glo HD": "Kobo Glo HD",
    "Kobo Glo": "Kobo Glo",
    "Kobo Libra H2O": "Kobo Libra H2O",
    "Kobo Mini/Touch": "Kobo Mini/Touch",
}

FORMAT_NAMES = {
    "MOBI/AZW3": "MOBI/AZW3",
    "EPUB": "EPUB",
    "CBZ": "CBZ",
    "Folder of images": "图片文件夹",
    "PDF": "PDF",
    "PDF (200MB limit)": "PDF（限 200MB）",
    "KFX (Send to Kindle EPUB)": "KFX（Send to Kindle 用 EPUB）",
    "MOBI + EPUB": "MOBI + EPUB",
    "EPUB (200MB limit)": "EPUB（限 200MB）",
    "MOBI + EPUB (200MB limit)": "MOBI + EPUB（限 200MB）",
}
