## ⚠️ 请先阅读

- **本版本在 AI 辅助下完成**：界面翻译、代码改动与文档均由 AI 生成，未经人工逐条校对，可能存在不准确之处。
- **非官方版本**：与 KCC 原作者无关联、未获其审核或背书。
- **仅限非商业使用**：程序图标采用 CC BY-NC-SA 3.0 许可。
- **本 Release 不包含 kindlegen**：该文件为亚马逊专有软件，许可不允许再分发。MOBI 转换请自行安装 Kindle Previewer。

---

## 下载

| 文件 | 说明 |
|---|---|
| `KCC_11.2.0_zh.exe` | Windows 单文件程序（约 84 MB），双击即用，无需安装 Python |

**SHA256 校验值**：

```
ab8db6e5769c0aefd934106b8f595885319b322f43ee7683f83e03dee15fc91c
```

下载后可执行 `certutil -hashfile KCC_11.2.0_zh.exe SHA256` 核对，或对照附件 `SHA256SUMS.txt`。

> **首次运行弹出「Windows 已保护你的电脑」？** 这是 SmartScreen 对未签名程序的常规提示——
> 本 exe 由源码直接构建、未购买代码签名证书，不代表有病毒。点击「更多信息」→「仍要运行」即可。
> 不放心的话可按仓库 README 第七节自行从源码构建。

> 需要 **MOBI 输出**的话，请另外安装 [Kindle Previewer](https://www.amazon.com/Kindle-Previewer/b?ie=UTF8&node=21381691011)（免费），
> KCC 会自动找到其中的 kindlegen。若只想输出 **CBZ/PDF/EPUB/KEPUB**，则无需任何额外依赖。

---

## 这是什么

基于 **Kindle Comic Converter 11.2.0** 官方源码的**完整简体中文化**版本。

把漫画/条漫转换成电子墨水阅读器专用格式，页面满屏无白边、支持固定版式。

- 输入：图片文件夹、CBZ/ZIP、CBR/RAR、CB7/7Z、PDF
- 输出：MOBI/AZW3、EPUB、KEPUB、CBZ、PDF、图片文件夹
- 支持设备：Kindle 全系、Kobo 全系、reMarkable 等 45 种设备配置

---

## 汉化范围

- 界面文字共约 **360 处**替换，覆盖主窗口、元数据编辑器、跨页标注对话框、
  全部状态提示与错误对话框、40+ 条工具提示
- 运行界面全量扫描：**189 条可见文字，0 条英文残留**
- 设备型号名（如 Kindle Oasis、Kobo Clara 2E）**保留英文**，方便对照商品页面；
  彩色机型额外标注「（彩色）」

---

## 为汉化所做的必要代码改动

原版 KCC 有两处如果只翻译文字就会出问题，本版本已修复：

| 位置 | 问题 | 修复方式 |
|---|---|---|
| 设备/格式下拉框 | 原代码用**显示出来的英文文字**作为字典键去查内部代码。只翻译文字会导致每次点「开始转换」都抛 `KeyError` | 改为「中文显示 + 英文键值」分离，19 处查找改用 `currentData()` |
| 跨页标注对话框 | 原代码靠比较标签文字 `"not a spread"` 判断状态。翻译后会**静默出错**（跨页标记写反、`list.remove` 抛异常） | 改用独立布尔状态变量 |

转换引擎本身**未做任何修改**。

---

## 验证情况

在 Windows 11 + Python 3.13 上完成：

- **回归测试**：45 个设备配置 + 10 种输出格式逐一遍历，**0 错误**
- **界面扫描**：遍历运行中窗口的 189 条可见文字，**0 条英文残留**
- **端到端转换**：CBZ / PDF / EPUB / MOBI / KEPUB 全部成功产出
- **打包产物已验证**：本 Release 的 exe 完成 MOBI 转换，过程日志全中文

```
[1/1] 源文件： test.cbz
正在生成 EPUB 文件…… 完成！
正在生成 MOBI 文件…… 完成！
正在处理 MOBI 文件…… 完成！
全部任务已完成。
```

---

## 常见问题

**Q：转换后 Kindle 上出现空白页？**
A：Kindle Scribe 用 PNG、Kindle Colorsoft 用任意格式都可能出现。改用 JPG 或 PDF 输出即可。

**Q：翻页慢、白边大？**
A：多半是传输时被第三方软件（如 Calibre）改动了。请直接用 USB 拖入设备的 `documents` 目录。
**不要用 Calibre 打开或修改输出文件。**

**Q：没有 kindlegen 能用吗？**
A：能。CBZ / PDF / EPUB / KEPUB 都不需要；只有 MOBI 需要，请安装 Kindle Previewer。

**Q：怎么切换回英文？**
A：本版是就地替换文字，不支持中英切换。英文原版请到 [上游仓库](https://github.com/ciromattia/kcc/releases) 下载。

---

## 许可证与合规

| 组件 | 许可 | 义务 |
|---|---|---|
| KCC 本体 | ISC | 保留版权与许可声明（本仓库完整保留 `LICENSE.txt`） |
| `dualmetafix.py` | GPL-3 | 分发二进制时需提供对应源码（本仓库含完整源码） |
| `image.py`（源自 Mangle） | GPL-3 | 同上 |
| 程序图标（Nikolay Verin 作） | CC BY-NC-SA 3.0 | 需署名、相同方式共享、**禁止商业使用** |

**本 Release 的 exe 因内含上述图标，仅限非商业使用。**

### 本 Release 不包含

- ❌ `kindlegen.exe`（亚马逊专有软件，许可不允许再分发）
- ❌ 任何亚马逊官方软件或电子书内容

---

## 致谢与免责

KCC 由 **Ciro Mattia Gonano**、**Paweł Jastrzębski**、**Darodi**、**Alex Xu** 开发，
官方项目：https://github.com/ciromattia/kcc

本仓库仅为界面汉化的非官方修改版。软件按「原样」提供，不附带任何担保，
使用风险由使用者自行承担。若上游作者认为本项目存在不妥，请联系删除。
