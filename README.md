> 🌐 **简体中文（默认）** | [English · 上游原文](README_upstream.md) | [上游文档中文翻译（AI 生成）](README_upstream_zh.md) | [上游分叉镜像](https://github.com/mengmengma0104/kcc)

[![版本](https://img.shields.io/github/v/release/mengmengma0104/kcc-zh-cn?label=%E7%89%88%E6%9C%AC&color=blue)](https://github.com/mengmengma0104/kcc-zh-cn/releases/latest)
[![下载量](https://img.shields.io/github/downloads/mengmengma0104/kcc-zh-cn/total?label=%E4%B8%8B%E8%BD%BD&color=success)](https://github.com/mengmengma0104/kcc-zh-cn/releases/latest)
[![许可证](https://img.shields.io/badge/%E8%AE%B8%E5%8F%AF%E8%AF%81-ISC-green)](LICENSE.txt)
[![平台](https://img.shields.io/badge/%E5%B9%B3%E5%8F%B0-Windows-lightgrey)](#一快速开始)
[![内容由 AI 生成](https://img.shields.io/badge/%E5%86%85%E5%AE%B9%E7%94%B1-AI%20%E7%94%9F%E6%88%90-orange)](#八许可证与合规)

# KCC 漫画转换器 11.3.2（简体中文汉化版）

![KCC 简体中文汉化版实际运行界面](docs/screenshot.png)

> ## ⚠️ 请先阅读
>
> - **本项目在 AI 辅助下完成**。界面翻译、代码改动与本文档均由 AI 生成，未经人工逐条校对。
>   翻译可能存在不准确、用词不当甚至理解错误之处。请自行评估后再决定是否使用。
> - **本仓库是非官方修改版**，与 KCC 原作者（Ciro Mattia Gonano、Paweł Jastrzębski、Darodi、Alex Xu）**没有任何关系**，
>   未获其背书或审核。遇到问题请勿向原作者反馈。
> - **本仓库不附带 `kindlegen.exe`**。该文件是亚马逊的专有软件，其许可**不允许再分发**，
>   因此本仓库不提供、也不随 Release 一起分发。MOBI 转换所需的 kindlegen 请自行获取（见第三节）。
> - **仅限非商业使用**。程序图标采用 CC BY-NC-SA 3.0 许可，禁止商业用途。详见第八节。

**Kindle Comic Converter（KCC）** 是一款把漫画、条漫、轻小说转换成电子墨水阅读器专用格式的工具。
转换后的页面可以**满屏无白边**显示，并支持固定版式。

本版本基于官方 **11.3.2** 源码完整汉化，仅界面文字改为简体中文，转换引擎与官方完全一致。

---

## 一、快速开始

1. 双击 `KCC_11.3.2_zh.exe` 启动程序（首次启动稍慢，属于正常现象）。
2. 把漫画文件或图片文件夹**拖入窗口**，或点击「添加输入文件」/「添加输入文件夹」。
3. 在右上角选择你的**设备**，在左上角选择**输出格式**。
4. 点击「开始转换」。转换完成后，输出文件会和源文件放在同一目录（或你指定的目录）。
5. 用 USB 把生成的 `.mobi` / `.kepub.epub` / `.pdf` 文件拖进设备的 **documents 文件夹**。

> **重要**：请**不要**用 Calibre 打开或修改 KCC 的输出文件。Calibre 对固定版式 EPUB/MOBI 支持不佳，
> 即使只改元数据也可能破坏版式、导致页码错乱。直接用 USB 拖入设备即可。

### 下载与安全校验

- 程序本体在 [Releases 页面](https://github.com/mengmengma0104/kcc-zh-cn/releases/latest)下载：
  `KCC_11.3.2_zh.exe`（约 91 MB，单文件免安装）。
- **SHA256 校验值**：
  `05d1cb189151f62c559aba682556cc7e1072c7918057259777cf35b561f2f8e0`
  下载后可在命令行执行 `certutil -hashfile KCC_11.3.2_zh.exe SHA256` 核对，或对照 Release 附件中的 `SHA256SUMS.txt`。
- **首次运行弹出「Windows 已保护你的电脑」？** 这是 Windows SmartScreen 对**未签名程序**的常规提示——
  本 exe 由源码直接构建，没有购买代码签名证书，并不代表有病毒。点击「更多信息」→「仍要运行」即可。
  如果不放心，可以跳过下载、按第七节自行从源码构建。

---

## 二、支持的格式

### 输入格式

| 格式 | 说明 |
|---|---|
| 图片文件夹 | 包含 JPG、PNG、GIF、WebP 的目录 |
| CBZ、ZIP | **需要 7-Zip** |
| CBR、RAR | **需要 7-Zip** |
| CB7、7Z | **需要 7-Zip** |
| PDF | 仅提取其中的 JPG 图像 |

### 输出格式

| 格式 | 适用设备 |
|---|---|
| **MOBI/AZW3** | 所有 Kindle（最常用） |
| **EPUB** | 通用；选择 Kobo 设备时自动输出 KEPUB |
| **KEPUB** | Kobo（选择 Kobo 设备 + EPUB 格式即可） |
| **CBZ** | 越狱 Kindle 装 KOreader、Kindle DX |
| **PDF** | reMarkable、Kindle Scribe 2025 |
| **图片文件夹** | 自行二次处理 |

> 关于 AZW3：KCC 生成的 `.mobi` 文件其实是 **MOBI 与 AZW3 双格式**，扩展名保持 `.mobi`
> 只是为了兼容性，无需另外转换。

---

## 三、可选依赖（用于增强功能）

程序**不装这些也能用**，但部分功能会受限。安装后需**重启 KCC** 才会被识别。

### 1. KindleGen（MOBI 转换必需）

KCC 生成 MOBI 依赖亚马逊官方的 `kindlegen` 工具。

- **推荐方式**：安装 [Kindle Previewer](https://www.amazon.com/Kindle-Previewer/b?ie=UTF8&node=21381691011)（免费），
  KCC 会自动从中找到 kindlegen，无需手动配置。
- **如果你已经有** `kindlegen.exe`：把它放在 `KCC_11.3.2_zh.exe` **同一个文件夹**里，程序会自动识别。

> **本仓库为何不附带 kindlegen？**
> `kindlegen` 是亚马逊的专有软件，其许可**明确不允许再分发**（仅授权安装使用，不允许转载、不允许通过网络分发）。
> 上游 KCC 项目也因此从不把 kindlegen 放进仓库或发布资源。
> 本仓库同样严格遵守这一点：**不提供该文件**，请通过安装 Kindle Previewer 自行获取。

> 提示：如果只想转换成 **CBZ** 或 **PDF**，则完全不需要 kindlegen。

### 2. 7-Zip（处理压缩包、元数据编辑）

处理 CBZ/CBR/CB7/RAR/ZIP 等压缩包以及使用元数据编辑器时需要。
KCC 会自动查找 `C:\Program Files\7-Zip`，安装到默认路径即可。

- 下载：https://www.7-zip.org/

---

## 四、常用选项说明

界面上每个选项**悬停鼠标即可看到详细说明**（已全部汉化）。几个最常用的：

| 选项 | 建议 |
|---|---|
| **条漫模式** | 韩式竖长条漫画请勾选 |
| **裁剪模式** | 默认「边距 + 页码」，一般保持默认 |
| **从右到左（漫画）** | 日式漫画勾选 |
| **彩色模式** | 想保留彩色时勾选（否则转灰度） |
| **JPEG/PNG/mozJpeg** | 黑白漫画用默认 JPEG 即可；mozJpeg 体积更小但耗时翻倍 |
| **跨页拆分** | 处理跨页大图时使用；可先用「标注跨页」按钮手工指定 |
| **禁用图像处理** | 只想原样打包、不做任何图像优化时勾选 |
| **文件合并** | 把多个文件（如各章节）合并成一册 |
| **输出分卷** | 自动按体积拆分，或把每个子目录当作一卷 |

---

## 五、常见问题

**Q：转换后 Kindle 上出现空白页？**
A：Kindle Scribe 使用 PNG 时、Kindle Colorsoft 使用任意格式时都可能出现。
改用 **JPG**（Scribe）或改用 **PDF** 输出可解决。往回翻几页再退出重进也能临时恢复。

**Q：翻页特别慢、白边特别大？**
A：多半是传输过程中被第三方软件（如 Calibre）改动了文件。请直接用 USB 把生成的文件拖入 `documents` 目录。

**Q：为什么选择 Kobo 设备后输出的是 `.kepub.epub`？**
A：这是正确行为。Kobo 设备使用 KEPUB 格式；如需普通 EPUB，勾选「不输出 KEPUB」相关选项。

**Q：KEPUB 选项在哪？**
A：选择任意 **Kobo** 设备 + **EPUB** 格式，输出即为 KEPUB。

**Q：右边到左边模式没生效？**
A：「从右到左」只影响 CBZ 输出的页面排列顺序；实际翻页方向由阅读器自身设置决定。

**Q：颜色反了？**
A：关闭 Kindle 的深色模式。

**Q：macOS 无法连接 Kindle Scribe 或 2024 年后的 Kindle？**
A：请使用亚马逊官方的 MTP 传输工具（Amazon USB File Transfer app）。

**Q：转换到一半想取消？**
A：点击「中止」按钮。转换过程可能不会立即停止，请稍等片刻。

**Q：程序界面有英文残留吗？**
A：设备型号名（如 Kindle Oasis、Kobo Clara 2E）刻意保留原文，方便对照网购页面。

---

## 六、汉化说明与已知限制

- 汉化方式为**直接替换界面文字**：程序结构、转换算法与官方 11.3.2 完全一致，只是文字改成中文。
- **本项目在 AI 辅助下完成**，翻译由 AI 生成、未经人工逐条校对，可能存在不准确之处。界面文字为就地替换，**不支持中英切换**；如需英文原版，请从官方仓库下载：https://github.com/ciromattia/kcc/releases
- 设备下拉框中，彩色机型额外标注了「（彩色）」以便区分。
- 本汉化版**仅包含图形界面程序**，不含命令行工具 `kcc-c2e` / `kcc-c2p`。
- 命令行工具的帮助信息、以及 `--help` 输出仍为英文（未纳入汉化范围）。

### 为汉化所做的代码改动

为了让中文界面正常工作，对源码做了以下**必要**修改（均不改变转换逻辑）：

| 位置 | 改动 | 原因 |
|---|---|---|
| `KCC_gui.py` | 设备/格式下拉框改为「中文显示 + 英文键值」分离，19 处查找改用 `currentData()` | 原代码用**显示文字**作为字典键查内部代码，直接翻译会导致每次转换都崩溃 |
| `KCC_spread_label.py` | 跨页标注对话框改用布尔状态变量 | 原代码靠比较标签文字 `"not a spread"` 判断状态，翻译后会静默出错 |
| `KCC_gui.py` | 元数据编辑器批量编辑的 5 个字段标题 | 这些英文标题会直接显示在提示框中 |

---

## 七、自己重新构建

汉化后的源码已随附，可自行重新打包（首次构建约需 5–10 分钟）：

```bat
cd kcc-11.2.0-zh
py -3.13 -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt pyinstaller -i https://pypi.tuna.tsinghua.edu.cn/simple
venv\Scripts\python.exe -m PyInstaller --hidden-import=_cffi_backend -y -F -i icons\comic2ebook.ico -n KCC_11.3.2_zh -w --noupx kcc.py
```

> 用 `python -m PyInstaller` 而非直接调 `pyinstaller.exe`：venv 若被移动过，
> pip 生成的入口程序内嵌旧路径会静默失效（rc=1 无输出），模块方式不受影响。

产物为 `dist\KCC_11.3.2_zh.exe`（约 91 MB）。
构建前请自行把 `kindlegen.exe` 放在 exe 同目录，否则 MOBI 转换不可用。

汉化相关工具位于 `tools\zh\`：

| 文件 | 作用 |
|---|---|
| `translations.py` | 英文→中文对照表（含 f-string 片段表，可自行增改） |
| `apply_zh.py` | 把对照表应用到 `.py` 与 `.ui` 两层源码（AST 精确替换，保留占位符） |
| `extract_strings.py` | 从源码提取待译字符串，生成对照表骨架 |
| `strict_audit.py` | 无白名单严格审计：列出所有可能漏译的英文字符串 |
| `test_gui_offscreen.py` | 离屏回归：遍历全部设备/格式 + 工具提示抽查 + 严格英文扫描 |
| `verify_invariants.py` | 校验键值分离不变量（字典键、下拉顺序、查找方式） |
| `scan_widget_strings.py` | 导出运行时界面全部可见文字，便于人工核对 |
| `capture_screenshot.py` | 启动 exe 截取界面并做像素质检 |
| `test_convert.py` | 端到端转换测试（CBZ/PDF/EPUB/KEPUB/MOBI） |
| `verify_commit_safe.py` | 预提交守卫：确认无 kindlegen、无可执行文件入库 |
| `audit_sync_fork.py` | 双仓库 blob 级比对与同步（经 GitHub API） |

---

## 八、许可证与合规

### 上游许可（ISC）

KCC 本体由 Ciro Mattia Gonano、Paweł Jastrzębski、Darodi、Alex Xu 开发，
以 **ISC 许可证**发布。该许可允许使用、复制、修改和分发，包括公开分发修改版，
**前提是保留版权声明与许可声明**。因此本仓库完整保留了上游的 `LICENSE.txt`，未作任何改动。

- 官方项目：https://github.com/ciromattia/kcc

### GPL-3 组件

以下两个文件来自 GPL-3 许可的第三方代码，分发编译产物时需同时提供对应源码：

| 文件 | 来源 | 许可 |
|---|---|---|
| `kindlecomicconverter/dualmetafix.py` | K. Hendricks 的 DualMetaFix | GPL-3 |
| `kindlecomicconverter/image.py` | Alex Yatskov 的 Mangle 及后续补丁 | GPL-3 |

本仓库包含**完整源代码**，满足源码提供义务。

### 图标许可（重要：限制商业使用）

程序图标由 **Nikolay Verin**（http://ncrow.deviantart.com/）创作，
采用 **CC BY-NC-SA 3.0** 许可（https://creativecommons.org/licenses/by-nc-sa/3.0/）。

这意味着：

- ✅ 允许非商业性地复制、分发、修改
- ✅ 必须**署名**作者 Nikolay Verin 并链接许可协议
- ✅ 修改后的图标必须以**相同许可**分发
- ❌ **禁止任何商业用途**（不得售卖、不得用于营利性服务、不得投放广告变现）

因此**本汉化版的编译产物（exe）仅限非商业使用**。

### 本仓库不包含的内容

- ❌ **`kindlegen.exe`** —— 亚马逊专有软件，许可不允许再分发（原因见第三节）
- ❌ 任何亚马逊官方软件、电子书内容

### 免责声明

本仓库为**非官方**的个人汉化项目，与上游作者无关联、未获其审核或背书。
本项目在 **AI 辅助下完成**，可能存在翻译错误。软件按"原样"提供，不附带任何担保，
使用风险由使用者自行承担。若上游作者认为本项目存在不妥，请联系删除。

