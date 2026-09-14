# -*- coding: utf-8 -*-
"""Simplified-Chinese translation table for KCC 11.2.0.

Two sections:
  UI        -> strings living in gui/*.ui and the generated KCC_ui.py / KCC_ui_editor.py
  MESSAGES  -> runtime strings in KCC_gui.py / KCC_spread_label.py / shared.py

Rules honoured here:
  * placeholders (%s, %d, {}, {0}, %.2f) are preserved verbatim and in order
  * HTML tags/attributes are preserved; only human-visible text is translated
  * profile / format keys, sentinels ('ARISE', 'Separator', 'Other'), file
    extensions, URLs, package names and brand/model names are NOT translated
"""

# ---------------------------------------------------------------------------
# UI: widget labels, buttons, group titles, window titles
# ---------------------------------------------------------------------------
UI = {
    # windows / titles
    "Kindle Comic Converter": "Kindle 漫画转换器",
    "Metadata editor": "元数据编辑器",
    "Metadata Editor": "元数据编辑器",

    # push buttons / short labels
    "Clear list": "清空列表",
    "Add input folder(s)": "添加输入文件夹",
    "Add input file(s)": "添加输入文件",
    "Convert": "开始转换",
    "Abort": "中止",
    "Save": "保存",
    "Cancel": "取消",
    "Label Spreads": "标注跨页",
    "Support me on Ko-fi": "在 Ko-fi 上支持我",
    "Humble Bundle Referral": "Humble Bundle 推广",
    "Toggle Easy/Expert Mode": "切换简易/专家模式",
    "Easy/Expert Mode": "简易/专家模式",

    # option labels
    "Preserve Margin %": "保留边距 %",
    "Cropping power:": "裁剪力度：",
    "Gamma: Auto": "伽马：自动",
    "Gamma: ": "伽马：",
    "Cropping Power: ": "裁剪力度：",
    "Custom height:": "自定义高度：",
    "Custom width:": "自定义宽度：",
    "Panel View 4/2/HQ": "面板视图 4/2/高质量",
    "Legacy Extract": "旧版提取方式",
    "Output split": "输出分卷",
    "Temp Directory": "临时目录",
    "Disable processing": "禁用图像处理",
    "Stretch/Upscale": "拉伸/放大",
    "Inter-panel crop": "面板间裁剪",
    "EPUB language": "EPUB 语言",
    "Default Author": "默认作者",
    "Default Author is KCC": "默认作者为 KCC",
    "Default Title": "默认标题",
    "Webtoon mode": "条漫模式",
    "No rotate": "不旋转",
    "Delete input": "删除源文件",
    "Invert Direction": "反转翻页方向",
    "No Quantize": "不做色彩量化",
    "Rotate First": "旋转页优先",
    "Rotate Right": "向右旋转",
    "Cropping mode": "裁剪模式",
    "JPEG/PNG/mozJpeg": "JPEG/PNG/mozJpeg",
    "Light novel mode": "轻小说模式",
    "Metadata Title": "元数据标题",
    "File Fusion": "文件合并",
    "Force PNG RGB": "强制 PNG RGB",
    "Wallpaper mode": "壁纸模式",
    "1x4 to 2x2 strips": "1x4 转 2x2 条带",
    "Extreme Black Point": "极值黑点",
    "Force EBOK": "强制 EBOK",
    "PDF Width Render": "PDF 按宽度渲染",
    "Custom Autocontrast": "自定义自动对比度",
    "Output Folder": "输出文件夹",
    "PNG Legacy Mode": "PNG 兼容模式",
    "Vertical 4 Panel": "垂直四面板",
    "W/B margins": "黑白边距",
    "Rainbow eraser": "彩虹纹消除",
    "WebP (experimental)": "WebP（实验性）",
    "Spread splitter": "跨页拆分",
    "Chunk size": "分块大小",
    "Chunk size MB:": "分块大小 MB：",
    "Custom JPEG Quality": "自定义 JPEG 质量",
    "Custom gamma": "自定义伽马",
    "Right-to-left (manga)": "从右到左（漫画）",
    "Color mode": "彩色模式",
    "Cover Fill": "封面填充",
    "Smart Cover Crop": "智能封面裁剪",
    "Spread shift": "跨页偏移",
    "1 Page Landscape": "单页横向",
    "Keep ComicInfo.xml": "保留 ComicInfo.xml",
    "JPEG Quality:": "JPEG 质量：",

    # metadata editor field labels
    "Series:": "系列：",
    "Volume:": "卷号：",
    "Number:": "期号：",
    "Writer:": "编剧：",
    "Penciller:": "作画：",
    "Inker:": "墨线：",
    "Colorist": "上色：",
    "Colorist:": "上色：",
    "Title:": "标题：",

    # ------------------------------------------------------------------
    # tooltips (HTML from gui/KCC.ui) — tags kept, text translated
    # ------------------------------------------------------------------
    "<html><head/><body><p>Double click on source to open it in metadata editor.</p></body></html>":
        "<html><head/><body><p>双击列表中的文件，可在元数据编辑器中打开。</p></body></html>",
    "<html><head/><body><p>After calculating the cropping boundaries, &quot;back up&quot; a specified percentage amount.</p></body></html>":
        "<html><head/><body><p>计算裁剪边界后，按指定百分比向外“回退”留白。</p></body></html>",
    "<html><head/><body><p style='white-space:pre'>Resolution of the target device.</p></body></html>":
        "<html><head/><body><p style='white-space:pre'>目标设备的分辨率。</p></body></html>",
    "<html><head/><body><p style='white-space:pre'>Add directory containing JPG, PNG or GIF files to queue.<br/><span style=\" font-weight:600;\">CBR, CBZ and CB7 files inside will not be processed!</span></p></body></html>":
        "<html><head/><body><p style='white-space:pre'>把包含 JPG、PNG 或 GIF 文件的目录加入队列。<br/><span style=\" font-weight:600;\">目录内的 CBR、CBZ 和 CB7 文件不会被处理！</span></p></body></html>",
    "<html><head/><body><p style='white-space:pre'>Output format.</p></body></html>":
        "<html><head/><body><p style='white-space:pre'>输出格式。</p></body></html>",
    "<html><head/><body><p style='white-space:pre'>Target device.</p></body></html>":
        "<html><head/><body><p style='white-space:pre'>目标设备。</p></body></html>",
    "<html><head/><body><p style='white-space:pre'>Add CBR, CBZ, CB7 or PDF file to queue.</p></body></html>":
        "<html><head/><body><p style='white-space:pre'>把 CBR、CBZ、CB7 或 PDF 文件加入队列。</p></body></html>",
    "<html><head/><body><p style='white-space:pre'>Shift+Click to select the output directory for this list.</p></body></html>":
        "<html><head/><body><p style='white-space:pre'>按住 Shift 点击，可为该列表单独指定输出目录。</p></body></html>",
    "<html><head/><body><p style='white-space:pre'>Enable right-to-left reading.</p></body></html>":
        "<html><head/><body><p style='white-space:pre'>启用从右到左阅读。</p></body></html>",
    "<html><head/><body><p style='white-space:pre'>Disable conversion to grayscale.</p></body></html>":
        "<html><head/><body><p style='white-space:pre'>不做灰度转换（保留彩色）。</p></body></html>",
    "<html><head/><body><p style='white-space:pre'>Enable special parsing mode for Korean Webtoons.</p></body></html>":
        "<html><head/><body><p style='white-space:pre'>启用韩式条漫的特殊解析模式。</p></body></html>",
    "<html><head/><body><p style='white-space:pre'>Do not process any image, ignore profile and processing options.</p></body></html>":
        "<html><head/><body><p style='white-space:pre'>不对图像做任何处理，忽略配置文件和图像处理选项。</p></body></html>",
    "<html><head/><body><p style='white-space:pre'>Shift+Click to edit directory.</p></body></html>":
        "<html><head/><body><p style='white-space:pre'>按住 Shift 点击可编辑目录。</p></body></html>",
    "<html><head/><body><p style='white-space:pre'><span style=\" font-weight:600; text-decoration: underline;\">Unchecked - 4 panels<br/></span>Zoom each corner separately.</p><p style='white-space:pre'><span style=\" font-weight:600; text-decoration: underline;\">Indeterminate - 2 panels<br/></span>Zoom only the top and bottom of the page.</p><p><span style=\" font-weight:600; text-decoration: underline;\">Checked - 4 high-quality panels<br/></span>Zoom each corner separately. Try to increase the quality of magnification. Check wiki for more details.</p></body></html>":
        "<html><head/><body><p style='white-space:pre'><span style=\" font-weight:600; text-decoration: underline;\">未勾选 - 4 面板<br/></span>分别放大四个角。</p><p style='white-space:pre'><span style=\" font-weight:600; text-decoration: underline;\">半选 - 2 面板<br/></span>只放大页面的顶部和底部。</p><p><span style=\" font-weight:600; text-decoration: underline;\">勾选 - 4 个高质量面板<br/></span>分别放大四个角，并尽量提高放大质量。详见 wiki。</p></body></html>",
    "<html><head/><body><p style='white-space:pre'><span style=\" font-weight:600; text-decoration: underline;\">Unchecked - Automatic mode<br/></span>The output will be split automatically.</p><p style='white-space:pre'><span style=\" font-weight:600; text-decoration: underline;\">Checked - Volume mode<br/></span>Every subdirectory will be considered as a separate volume.</p></body></html>":
        "<html><head/><body><p style='white-space:pre'><span style=\" font-weight:600; text-decoration: underline;\">未勾选 - 自动模式<br/></span>输出文件会自动分卷。</p><p style='white-space:pre'><span style=\" font-weight:600; text-decoration: underline;\">勾选 - 分卷模式<br/></span>每个子目录视为独立的一卷。</p></body></html>",
    "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">Unchecked - Main Drive<br/></span>Use dedicated temporary directory on main OS drive.</p><p><span style=\" font-weight:600; text-decoration: underline;\">Checked - Source File Drive<br/></span>Create temporary file directory on source file drive.</p></body></html>":
        "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">未勾选 - 主硬盘<br/></span>在系统主硬盘上使用专用临时目录。</p><p><span style=\" font-weight:600; text-decoration: underline;\">勾选 - 源文件所在盘<br/></span>在源文件所在磁盘创建临时目录。</p></body></html>",
    "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">Unchecked - Nothing<br/></span>Images smaller than device resolution will not be resized.</p><p><span style=\" font-weight:600; text-decoration: underline;\">Indeterminate - Stretching<br/></span>Images smaller than device resolution will be resized. Aspect ratio will be not preserved.</p><p><span style=\" font-weight:600; text-decoration: underline;\">Checked - Upscaling<br/></span>Images smaller than device resolution will be resized. Aspect ratio will be preserved.</p></body></html>":
        "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">未勾选 - 不处理<br/></span>小于设备分辨率的图像不缩放。</p><p><span style=\" font-weight:600; text-decoration: underline;\">半选 - 拉伸<br/></span>小于设备分辨率的图像会被缩放，不保持宽高比。</p><p><span style=\" font-weight:600; text-decoration: underline;\">勾选 - 放大<br/></span>小于设备分辨率的图像会被缩放，并保持宽高比。</p></body></html>",
    "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">Unchecked - Disabled<br/></span>Disabled</p><p><span style=\" font-weight:600; text-decoration: underline;\">Indeterminate - Horizontal<br/></span>Crop empty horizontal lines.</p><p><span style=\" font-weight:600; text-decoration: underline;\">Checked - Both<br/></span>Crop empty horizontal and vertical lines.</p></body></html>":
        "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">未勾选 - 禁用<br/></span>禁用</p><p><span style=\" font-weight:600; text-decoration: underline;\">半选 - 横向<br/></span>裁掉空白横向条带。</p><p><span style=\" font-weight:600; text-decoration: underline;\">勾选 - 双向<br/></span>裁掉空白横向和纵向条带。</p></body></html>",
    "<html><head/><body><p>Default EPUB language is en-US.</p><p>Only use if your EPUB reader has problems with English fonts.</p></body></html>":
        "<html><head/><body><p>默认 EPUB 语言为 en-US。</p><p>仅在您的 EPUB 阅读器对英文字体有问题时才需要修改。</p></body></html>",
    "<html><head/><body><p>Invert the page turn direction.</p><p>Usually used with right to left manga but you want to page turn left to right. Spread splitting would still be right to left in this case.</p><p>Will break various features like landscape mode order.</p></body></html>":
        "<html><head/><body><p>反转翻页方向。</p><p>通常用于从右到左的漫画，但您希望从左到右翻页的情况。此时跨页拆分仍按从右到左处理。</p><p>会破坏横向模式顺序等功能。</p></body></html>",
    "<html><head/><body><p>When the spread splitter option is partially checked,</p><p><span style=\" font-weight:600; text-decoration: underline;\">Unchecked - Rotate Last<br/></span>Put the rotated 2 page spread after the split spreads.</p><p><span style=\" font-weight:600; text-decoration: underline;\">Checked - Rotate First<br/></span>Put the rotated 2 page spread before the split spreads.</p></body></html>":
        "<html><head/><body><p>当“跨页拆分”为半选状态时：</p><p><span style=\" font-weight:600; text-decoration: underline;\">未勾选 - 旋转页在后<br/></span>旋转后的跨页图排在拆分页之后。</p><p><span style=\" font-weight:600; text-decoration: underline;\">勾选 - 旋转页在前<br/></span>旋转后的跨页图排在拆分页之前。</p></body></html>",
    "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">Unchecked - Disabled</span></p><p>Disabled</p><p><span style=\" font-weight:600; text-decoration: underline;\">Indeterminate - Margins<br/></span>Margins</p><p><span style=\" font-weight:600; text-decoration: underline;\">Checked - Margins + page numbers<br/></span>Margins +page numbers</p></body></html>":
        "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">未勾选 - 禁用</span></p><p>禁用</p><p><span style=\" font-weight:600; text-decoration: underline;\">半选 - 裁边距<br/></span>只裁边距</p><p><span style=\" font-weight:600; text-decoration: underline;\">勾选 - 边距 + 页码<br/></span>边距和页码一起裁掉</p></body></html>",
    "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">Unchecked - JPEG<br/></span>Use JPEG files</p><p><span style=\" font-weight:600; text-decoration: underline;\">Indeterminate - force PNG<br/></span>Create PNG files instead JPEG for black and white images</p><p><span style=\" font-weight:600; text-decoration: underline;\">Checked - mozJpeg<br/></span>10-20% smaller JPEG file, with the same image quality, but processing time multiplied by 2</p></body></html>":
        "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">未勾选 - JPEG<br/></span>使用 JPEG 文件</p><p><span style=\" font-weight:600; text-decoration: underline;\">半选 - 强制 PNG<br/></span>黑白图像使用 PNG 而非 JPEG</p><p><span style=\" font-weight:600; text-decoration: underline;\">勾选 - mozJpeg<br/></span>画质不变，JPEG 体积小 10-20%，但处理时间翻倍</p></body></html>",
    "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">Unchecked - Don't use metadata Title<br/></span>Write default title.</p><p><span style=\" font-weight:600; text-decoration: underline;\">Indeterminate - Add metadata Title to the default schema<br/></span>Write default title with Title from ComicInfo.xml or other embedded metadata.</p><p><span style=\" font-weight:600; text-decoration: underline;\">Checked - Use metadata Title only<br/></span>Write Title from ComicInfo.xml or other embedded metadata.</p></body></html>":
        "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">未勾选 - 不使用元数据标题<br/></span>写入默认标题。</p><p><span style=\" font-weight:600; text-decoration: underline;\">半选 - 元数据标题追加到默认命名后<br/></span>默认标题后附加 ComicInfo.xml 等内嵌元数据中的标题。</p><p><span style=\" font-weight:600; text-decoration: underline;\">勾选 - 仅使用元数据标题<br/></span>仅使用 ComicInfo.xml 等内嵌元数据中的标题。</p></body></html>",
    "<html><head/><body><p>Combines all selected files into a single file. (Helpful for combining chapters into volumes.)</p></body></html>":
        "<html><head/><body><p>把所有选中文件合并为单个文件（便于把多个章节合并成卷）。</p></body></html>",
    "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">Unchecked - 1x4<br/></span>Keep format 1x4 panels strips.</p><p><span style=\" font-weight:600; text-decoration: underline;\">Checked - 2x2<br/></span>Turn 1x4 strips to 2x2 to maximize screen usage.</p></body></html>":
        "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">未勾选 - 1x4<br/></span>保持 1x4 面板条带。</p><p><span style=\" font-weight:600; text-decoration: underline;\">勾选 - 2x2<br/></span>把 1x4 条带改为 2x2，充分利用屏幕。</p></body></html>",
    "<html><head/><body><p>By default, KCC maps the darkest pixel value to pure black (the black point.)</p><p>Extreme black point sets the black point to be the most common dark pixel value.</p><p>Useful when text is black but artwork is gray.</p></body></html>":
        "<html><head/><body><p>默认情况下，KCC 把最暗的像素值映射为纯黑（黑点）。</p><p>“极值黑点”改为把最常见的暗像素值设为黑点。</p><p>适用于文字为黑、画面偏灰的情况。</p></body></html>",
    "<html><head/><body><p>Force Kindle MOBI to be be tagged as EBOK instead of PDOC.</p><p>This may cause USB loaded books to be deleted if you go online after a month offline.</p></body></html>":
        "<html><head/><body><p>强制把 Kindle MOBI 标记为 EBOK 而不是 PDOC。</p><p>若离线超过一个月后再联网，可能导致通过 USB 导入的书籍被删除。</p></body></html>",
    "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">Unchecked - BW only<br/></span>Only autocontrast bw pages. Ignored for pages where near blacks or whites don't exist.</p><p><span style=\" font-weight:600; text-decoration: underline;\">Indeterminate - Disabled<br/></span>Disable autocontrast</p><p><span style=\" font-weight:600; text-decoration: underline;\">Checked - BW and Color<br/></span>BW and color images will be autocontrasted. Ignored for pages where near blacks or whites don't exist.</p></body></html>":
        "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">未勾选 - 仅黑白<br/></span>只对黑白页面做自动对比度。页面中不存在接近纯黑或纯白的像素时跳过。</p><p><span style=\" font-weight:600; text-decoration: underline;\">半选 - 禁用<br/></span>禁用自动对比度</p><p><span style=\" font-weight:600; text-decoration: underline;\">勾选 - 黑白与彩色<br/></span>黑白和彩色图像都做自动对比度。页面中不存在接近纯黑或纯白的像素时跳过。</p></body></html>",
    "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">Unchecked - next to source<br/></span>Place output files next to source files</p><p><span style=\" font-weight:600; text-decoration: underline;\">Indeterminate - folder next to source<br/></span>Place output files in a folder next to source files</p><p><span style=\" font-weight:600; text-decoration: underline;\">Checked - Custom<br/></span>Place output files in custom directory specified by right button</p></body></html>":
        "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">未勾选 - 与源文件同目录<br/></span>输出文件放在源文件旁边</p><p><span style=\" font-weight:600; text-decoration: underline;\">半选 - 源文件旁的文件夹<br/></span>输出文件放在源文件旁的文件夹中</p><p><span style=\" font-weight:600; text-decoration: underline;\">勾选 - 自定义<br/></span>输出文件放在右侧按钮指定的自定义目录中</p></body></html>",
    "<html><head/><body><p>Use this to select the default output directory.</p></body></html>":
        "<html><head/><body><p>用于选择默认输出目录。</p></body></html>",
    "<html><head/><body><p>In virtual panel mode:</p><p><span style=\" font-weight:600; text-decoration: underline;\">Unchecked - Horizontal<br/></span>First two panels are the top panels.</p><p><span style=\" font-weight:600; text-decoration: underline;\">Checked - Vertical<br/></span>First two panels are the side panels.</p></body></html>":
        "<html><head/><body><p>在虚拟面板模式下：</p><p><span style=\" font-weight:600; text-decoration: underline;\">未勾选 - 横向<br/></span>前两个面板是顶部面板。</p><p><span style=\" font-weight:600; text-decoration: underline;\">勾选 - 纵向<br/></span>前两个面板是侧边面板。</p></body></html>",
    "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">Unchecked - Autodetection<br/></span>The color of margins fill will be detected automatically.</p><p><span style=\" font-weight:600; text-decoration: underline;\">Indeterminate - White<br/></span>Margins will be untouched.</p><p><span style=\" font-weight:600; text-decoration: underline;\">Checked - Black<br/></span>Margins will be filled with black color.</p></body></html>":
        "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">未勾选 - 自动检测<br/></span>自动检测边距填充颜色。</p><p><span style=\" font-weight:600; text-decoration: underline;\">半选 - 白色<br/></span>边距保持原样。</p><p><span style=\" font-weight:600; text-decoration: underline;\">勾选 - 黑色<br/></span>边距填充为黑色。</p></body></html>",
    "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">Unchecked - Split<br/></span>Double page spreads will be cut into two separate pages.</p><p><span style=\" font-weight:600; text-decoration: underline;\">Indeterminate - Split and rotate<br/></span>Double page spreads will be displayed twice. First split and then rotated. </p><p><span style=\" font-weight:600; text-decoration: underline;\">Checked - Rotate<br/></span>Double page spreads will be rotated.</p></body></html>":
        "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">未勾选 - 拆分<br/></span>跨页图裁成两个独立页面。</p><p><span style=\" font-weight:600; text-decoration: underline;\">半选 - 拆分并旋转<br/></span>跨页图显示两次：先拆分，再旋转。</p><p><span style=\" font-weight:600; text-decoration: underline;\">勾选 - 旋转<br/></span>跨页图旋转显示。</p></body></html>",
    "<html><head/><body><p><span style=\" font-weight:700; text-decoration: underline;\">Unchecked<br/></span>Maximal output file size is 100 MB for Webtoon, 400 MB for others before split occurs.</p><p><span style=\" font-weight:700; text-decoration: underline;\">Checked</span><br/>Output file size specified in &quot;Chunk size MB&quot; before split occurs.</p></body></html>":
        "<html><head/><body><p><span style=\" font-weight:700; text-decoration: underline;\">未勾选<br/></span>分卷前的最大输出体积：条漫 100 MB，其他 400 MB。</p><p><span style=\" font-weight:700; text-decoration: underline;\">勾选</span><br/>分卷前按“分块大小 MB”中指定的体积执行。</p></body></html>",
    "<html><head/><body><p>Set a custom gamma correction.</p><p>1.0 is default (disabled).<br/>&lt; 1.0 makes the image brighter.<br/>&gt; 1.0 makes the image darker. </p><p>1.8 was the default in KCC 9.1.0 and earlier.</p><p>Use if you want to make midtones darker.</p></body></html>":
        "<html><head/><body><p>设置自定义伽马校正。</p><p>默认 1.0（不生效）。<br/>&lt; 1.0 图像变亮。<br/>&gt; 1.0 图像变暗。</p><p>KCC 9.1.0 及更早版本的默认值为 1.8。</p><p>如需让中间调变暗可使用此选项。</p></body></html>",
    "<html><head/><body><p>Default Title</p></body></html>":
        "<html><head/><body><p>默认标题</p></body></html>",
    "<html><head/><body><p>Attempt to crop main cover from wide image.</p></body></html>":
        "<html><head/><body><p>尝试从宽幅图像中裁出主封面。</p></body></html>",
    "<html><head/><body><p>Warning: chunk size greater than default may cause<br/>performance/battery issues, especially on older devices.</p></body></html>":
        "<html><head/><body><p>警告：分块大小高于默认值可能导致<br/>性能与耗电问题，老旧设备尤为明显。</p></body></html>",
    "<b>Tip:</b> Hover mouse over options/buttons to see explanations. Boxes can be partially/fully checked.":
        "<b>提示：</b>把鼠标悬停在选项/按钮上可查看说明。复选框支持半选和全选。",
    "<b>Tip:</b> You can drag and drop image folders or comic files/archives into this window to convert.":
        "<b>提示：</b>可以把图片文件夹或漫画文件/压缩包直接拖入本窗口进行转换。",
    "<b>Tip:</b> Calibre may add margins! USB drop directly into the device's documents folder instead.":
        "<b>提示：</b>Calibre 可能会添加白边！建议直接用 USB 把文件拖入设备的 documents 文件夹。",
    "<b>Tip:</b> You can toggle easy/expert mode using button at top right.":
        "<b>提示：</b>可用右上角按钮切换简易/专家模式。",
    "Since you are a new user of <b>KCC</b> please see few <a href=\"https://github.com/ciromattia/kcc/wiki/Important-tips\">important tips</a>.":
        "您是 <b>KCC</b> 的新用户，请先看看这几条 <a href=\"https://github.com/ciromattia/kcc/wiki/Important-tips\">重要提示</a>。",
    "<a href=\"https://github.com/ciromattia/kcc#7-zip\">Install 7z (link)</a> to enable CBZ/CBR/ZIP/etc processing.":
        "<a href=\"https://github.com/ciromattia/kcc#7-zip\">安装 7z（链接）</a> 以启用 CBZ/CBR/ZIP 等格式的处理。",
    "<a href=\"https://github.com/ciromattia/kcc#7-zip\">Install 7z (link)</a> to enable metadata editing.":
        "<a href=\"https://github.com/ciromattia/kcc#7-zip\">安装 7z（链接）</a> 以启用元数据编辑。",
    "<b>Bulk Volume Editing</b><br>Check this box to assign volume numbers to multiple files.<br><br><b>Input formats:</b><br><code>5</code> → sequence starting from 5 (5, 6, 7...)<br><code>1-10</code> → range from 1 to 10<br><code>1, 3, 5</code> → specific values<br><br><i>Note: Files are sorted alphabetically before assignment.</i>":
        "<b>批量卷号编辑</b><br>勾选后可为多个文件批量指定卷号。<br><br><b>输入格式：</b><br><code>5</code> → 从 5 开始的序列（5, 6, 7……）<br><code>1-10</code> → 1 到 10 的范围<br><code>1, 3, 5</code> → 指定具体数值<br><br><i>注意：分配前会先按字母顺序对文件排序。</i>",
}

# ---------------------------------------------------------------------------
# MESSAGES: runtime strings emitted from code
# ---------------------------------------------------------------------------
MESSAGES = {
    # conversion progress / status
    "<b>Conversion interrupted.</b>": "<b>转换已中断。</b>",
    "Conversion interrupted.": "转换已中断。",
    "Attempting file fusion": "正在尝试合并文件",
    "Created fusion at ": "已生成合并文件：",
    "Fusion Failed. ": "合并失败。",
    "Process Failed. Custom title can't be set when processing more than 1 source.\nDid you forget to check fusion?":
        "处理失败。处理多个源文件时无法设置自定义标题。\n是否忘记勾选“文件合并”？",
    "Source:</b> ": "源文件：</b> ",
    "Creating CBZ files": "正在生成 CBZ 文件",
    "Creating folders": "正在生成图片文件夹",
    "Creating PDF files": "正在生成 PDF 文件",
    "Creating EPUB files": "正在生成 EPUB 文件",
    "Creating MOBI files": "正在生成 MOBI 文件",
    "Processing MOBI files": "正在处理 MOBI 文件",
    "Creating CBZ files... <b>Done!</b>": "正在生成 CBZ 文件…… <b>完成！</b>",
    "Creating folders... <b>Done!</b>": "正在生成图片文件夹…… <b>完成！</b>",
    "Creating PDF files... <b>Done!</b>": "正在生成 PDF 文件…… <b>完成！</b>",
    "Creating EPUB files... <b>Done!</b>": "正在生成 EPUB 文件…… <b>完成！</b>",
    "Creating MOBI files... <b>Done!</b>": "正在生成 MOBI 文件…… <b>完成！</b>",
    "Processing MOBI files... <b>Done!</b>": "正在处理 MOBI 文件…… <b>完成！</b>",
    "Kindle detected. Uploading covers... <b>Done!</b>": "检测到 Kindle，正在上传封面…… <b>完成！</b>",
    "Failed to process MOBI file!": "处理 MOBI 文件失败！",
    "KindleGen failed to create MOBI!": "KindleGen 生成 MOBI 失败！",
    "KindleGen error:\n\n": "KindleGen 错误：\n\n",
    "Created EPUB file was too big. Weird file structure?": "生成的 EPUB 文件过大。文件结构异常？",
    "MB. Supported size: ~350MB.": "MB。支持的体积约为 350MB。",
    "EPUB file: ": "EPUB 文件：",
    "<b>All jobs completed.</b>": "<b>全部任务已完成。</b>",
    "All jobs completed.": "全部任务已完成。",
    "Error during conversion!": "转换出错！",
    "Error during conversion! Please consult <a href=\"https://github.com/ciromattia/kcc/wiki/Error-messages\">wiki</a> for more details.":
        "转换出错！请查阅 <a href=\"https://github.com/ciromattia/kcc/wiki/Error-messages\">wiki</a> 了解详情。",
    "Error during conversion %s:\n\n%s\n\nTraceback:\n%s": "转换出错 %s：\n\n%s\n\n堆栈跟踪：\n%s",
    "Failed to parse metadata!\n\n%s\n\nTraceback:\n%s": "解析元数据失败！\n\n%s\n\n堆栈跟踪：\n%s",
    "Failed to save metadata!\n\n%s\n\nTraceback:\n%s": "保存元数据失败！\n\n%s\n\n堆栈跟踪：\n%s",
    "Unsupported file type for ": "不支持的文件类型：",

    # dialogs / questions
    "KCC - Error": "KCC - 错误",
    "KCC - Question": "KCC - 询问",
    "The process will be interrupted. Please wait.": "进程将被中断，请稍候。",
    "No files selected! Please choose files to convert.": "未选择文件！请先选择要转换的文件。",
    "Target resolution is not set!": "未设置目标分辨率！",
    "Cannot select Kindle as output directory": "不能把 Kindle 设为输出目录",
    "Select default output folder": "选择默认输出文件夹",
    "Select output directory": "选择输出目录",
    "Select file": "选择文件",
    "Select file(s)": "选择文件",
    "Select input folder(s)": "选择输入文件夹",
    "Select volume directories": "选择分卷目录",
    "Comic (*.cbz *.cbr *.cb7 *.zip *.rar *.7z *.epub *.pdf);;All (*.*)":
        "漫画文件 (*.cbz *.cbr *.cb7 *.zip *.rar *.7z *.epub *.pdf);;所有文件 (*.*)",
    "Comic (*.pdf);;All (*.*)": "漫画文件 (*.pdf);;所有文件 (*.*)",
    "Comic (*.cbz *.cbr *.cb7)": "漫画文件 (*.cbz *.cbr *.cb7)",

    # tool / capability hints
    "Editor is disabled due to a lack of 7z.": "由于缺少 7z，编辑器已被禁用。",
    "You can choose a taller device profile to get taller cuts in webtoon mode.":
        "在条漫模式下，可选择更高的设备配置以获得更高的分块。",
    "Try reading webtoon panels side by side in landscape!":
        "试试在横向模式下并排阅读条漫面板！",
    "This option is intended for older Kindle models.": "此选项针对较老的 Kindle 机型。",
    "On this device, there will be conversion speed and quality issues.":
        "在该设备上会出现转换速度和质量问题。",
    "Use the Kindle Scribe profile if you want higher resolution when zooming.":
        "如需在放大时获得更高分辨率，请使用 Kindle Scribe 配置。",
    "Scribe PNG MOBI/EPUB has a lot of problems like blank pages/sections. Use JPG instead.":
        "Scribe 使用 PNG 生成 MOBI/EPUB 时常出现空白页/空白段等问题，请改用 JPG。",
    "Colorsoft MOBI/EPUB can have blank pages. Just go back a few pages, exit, and reenter book.":
        "Colorsoft 的 MOBI/EPUB 可能出现空白页。往回翻几页、退出再重新进入书籍即可恢复。",
    "<a href=\"https://github.com/ciromattia/kcc/wiki/NonKindle-devices\">List of supported Non-Kindle devices.</a>":
        "<a href=\"https://github.com/ciromattia/kcc/wiki/NonKindle-devices\">非 Kindle 设备支持列表。</a>",
    "Partially check W/B Margins if you don't want KCC to extend the image margins.":
        "如果不希望 KCC 扩展图像边距，请把“黑白边距”设为半选。",
    "<a href=\"https://github.com/ciromattia/kcc#kindlegen\"><b>Install KindleGen (link)</b></a> to enable MOBI conversion for Kindles!":
        "<a href=\"https://github.com/ciromattia/kcc#kindlegen\"><b>安装 KindleGen（链接）</b></a> 以启用 Kindle 的 MOBI 转换！",
    "Your <a href=\"https://www.amazon.com/b?node=23496309011\">KindleGen</a> is outdated! MOBI conversion might fail.":
        "您的 <a href=\"https://www.amazon.com/b?node=23496309011\">KindleGen</a> 版本过旧！MOBI 转换可能失败。",
    "kindlegen: ": "kindlegen：",
    "\n\n Re-install Rosetta/Kindle Previewer/other Intel app?\n\nPlease email Amazon to make Kindle Previewer Apple silicon native at amazon.com/kindle-help":
        "\n\n 是否重新安装 Rosetta/Kindle Previewer/其他 Intel 应用？\n\n请发邮件给 Amazon，推动 Kindle Previewer 原生支持 Apple 芯片：amazon.com/kindle-help",
    "You can choose a taller device profile to get taller cuts in webtoon mode.":
        "在条漫模式下，可选择更高的设备配置以获得更高的分块。",

    # metadata editor / bulk editing
    "CBR files in selection are read-only.": "所选内容中的 CBR 文件为只读。",
    "Editing ": "正在编辑 ",
    " files.": " 个文件。",
    "(multiple files)": "（多个文件）",
    "(multiple values)": "（多个值）",
    "Separate authors with a comma.": "多个作者请用逗号分隔。",
    "No changes to apply.": "没有需要应用的更改。",
    "Processing ": "正在处理 ",
    ": CBR is read-only": "：CBR 为只读",
    "Some files failed to save:\n\n": "部分文件保存失败：\n\n",
    "\n...and ": "\n……另有 ",
    " more": " 个",
    "Errors occurred.": "发生错误。",
    "Successfully updated ": "已成功更新 ",
    " field must be a number.": " 字段必须是数字。",
    "Invalid range format (use start-end)": "范围格式无效（请使用 起始-结束）",
    "Volume numbers must be positive": "卷号必须为正数",
    "Invalid range: start > end": "范围无效：起始值大于结束值",
    "Invalid range format": "范围格式无效",
    "Invalid list format": "列表格式无效",
    "Volume number must be positive": "卷号必须为正数",
    "Invalid number": "数字无效",
    "No valid volume numbers parsed": "未解析出有效的卷号",
    "Volume count (": "卷号数量（",
    ") != file count (": "）与文件数量（",
    "e.g., 5 or 1-10 or 1,3,5": "例如：5 或 1-10 或 1,3,5",
    "<p><em>Note: Changing this field will overwrite all values in all selected files.</em></p>":
        "<p><em>注意：修改此字段会覆盖所有选中文件中的对应值。</em></p>",
    "<table border=\"1\" cellspacing=\"0\" cellpadding=\"0\"><tr><th style=\"padding:2px 6px; text-align:left;\">File</th><th style=\"padding:2px 6px; text-align:left;\">Value</th></tr>":
        "<table border=\"1\" cellspacing=\"0\" cellpadding=\"0\"><tr><th style=\"padding:2px 6px; text-align:left;\">文件</th><th style=\"padding:2px 6px; text-align:left;\">值</th></tr>",
    "<table border=\"1\" cellspacing=\"0\" cellpadding=\"0\"><tr><th style=\"padding:2px 6px; text-align:left;\">Value</th><th style=\"padding:2px 6px; text-align:right;\">Count</th></tr>":
        "<table border=\"1\" cellspacing=\"0\" cellpadding=\"0\"><tr><th style=\"padding:2px 6px; text-align:left;\">值</th><th style=\"padding:2px 6px; text-align:right;\">数量</th></tr>",

    # shared.py dependency check
    " is not installed!": " 未安装！",
    "ERROR: ": "错误：",

    # status bar links
    "README": "说明文档",
    "FAQ": "常见问题",
    "WIKI": "Wiki",
    "YOUTUBE": "YouTube",
    "TUTORIAL": "视频教程",
    "EMAIL": "联系作者",
    "DONATE": "捐赠",
    "FORUM": "论坛",
    "DISCORD": "Discord",

    # window title suffix
    "Kindle Comic Converter ": "Kindle 漫画转换器 ",
}

# ---------------------------------------------------------------------------
# 补充词条：多行工具提示与长说明。
# 多行键使用真实换行符，与源码中隐式拼接后的字面量一致；
# 若写成字面反斜杠序列则无法匹配（应用器按字符串值比对）。
# ---------------------------------------------------------------------------
UI.update({
    'Auto check various options intended for KOreader wallpapers.\n\nWill also crop images to fill the screen centered.':
        '自动勾选专为 KOreader 壁纸设计的各类选项。\n\n同时会裁剪图像以居中铺满屏幕。',
    'Do not rotate double page spreads in spread splitter option.':
        '在跨页拆分选项中不旋转跨页图。',
    "Delete input file(s) or directory. It's not recoverable!":
        '删除输入文件或目录。此操作不可恢复！',
    'Force full color images to be saved in lossless PNG format, dramatically increases the filesize.':
        '强制把全彩图像保存为无损 PNG，文件体积会大幅增加。',
    'Use a more compatible 8 bit PNG instead of 4 bit.':
        '使用兼容性更好的 8 位 PNG，而不是 4 位。',
    'Rotate 2 page spreads in opposite direction than normal.':
        '跨页图按相反方向旋转。',
    'Erase rainbow effect on color eink screen by attenuating interfering frequencies':
        '通过衰减干扰频率，消除彩色电子墨水屏的彩虹纹',
    'Shift first page to opposite side in landscape for two page spread alignment':
        '横向时把首页偏移到另一侧，以对齐跨页',
    'Hold shift while clicking for a low quality preview.':
        '按住 Shift 点击可生成低质量预览。',
    'Greater than default may cause performance issues on older ereaders.':
        '高于默认值可能导致老设备出现性能问题。',
    'Hover over each option/button to see an explanation! Options can be partially checked or fully checked!':
        '把鼠标悬停在每个选项/按钮上可查看说明！选项支持半选和全选！',
    'Use the PDF/EPUB image extraction method from older KCC versions. \n\nUse if standard extraction fails for whatever reason.':
        '使用旧版 KCC 的 PDF/EPUB 图片提取方式。\n\n标准提取方式因故失败时可尝试此项。',
    "Don't quantize PNG images to 16 colors (4 bit)\n\nThis will double file size but preserve all 256 colors (8 bit).\n\nEink only has 16 shades of gray so you probably don't want this.":
        '不把 PNG 图像量化为 16 色（4 位）\n\n这会使文件体积翻倍，但保留全部 256 色（8 位）。\n\n电子墨水屏只有 16 级灰阶，通常不建议开启。',
    'Only resize images and preserve original file structure.\n\nIgnores most options besides JPEG quality, color mode, output folder.':
        '仅缩放图像并保留原始文件结构。\n\n除 JPEG 质量、彩色模式、输出文件夹外，忽略大部分选项。',
    'Render vector PDFs to device width instead of height.\n\nUseful if you plan to crop a little off the top and bottom to fill screen.':
        '按设备宽度而非高度渲染矢量 PDF。\n\n如果打算裁掉上下少量边缘以填满屏幕，此选项很有用。',
    'Replace JPG with lossy WebP and PNG with lossless WebP. This includes the JPG Quality.\n\nIgnored for Kindle EPUB/MOBI and all PDF.':
        '用有损 WebP 替换 JPG、用无损 WebP 替换 PNG（JPEG 质量设置同样生效）。\n\n对 Kindle 的 EPUB/MOBI 以及所有 PDF 无效。',
    'The JPEG quality, on a scale from 0 (worst) to 95 (best). \n\nDefault is 85 for most devices besides Kindle Scribe and Colorsoft, which are 90.\n\nHigher values are larger and higher quality, and may resolve blank page issues.':
        'JPEG 质量，范围 0（最差）到 95（最好）。\n\n除 Kindle Scribe 和 Colorsoft（默认 90）外，多数设备默认 85。\n\n数值越高体积越大、质量越好，也可能解决空白页问题。',
    'Resize cover to exact device resolution by center-cropping to aspect ratio first.\nMay crop top/bottom or left/right depending on source aspect ratio. Not implemented for Kindle Scribe.':
        '先按宽高比居中裁剪，再把封面缩放到设备精确分辨率。\n根据源图宽高比，可能裁掉上下或左右。Kindle Scribe 不支持此功能。',
    'Keep any original ComicInfo.xml files.\n\nKeeping this file may crash some readers like the Kobo native CBZ reader.':
        '保留原有的 ComicInfo.xml 文件。\n\n保留该文件可能导致某些阅读器崩溃，例如 Kobo 自带的 CBZ 阅读器。',
    '<html><head/><body><p><span style=" font-weight:600; text-decoration: underline;">Unchecked - 2 page landscape<br/></span>2 viewports for left and right pages</p><p><span style=" font-weight:600; text-decoration: underline;">Checked - 1 page landscape<br/></span>A single centered viewport for 1 page</p></body></html>':
        '<html><head/><body><p><span style=" font-weight:600; text-decoration: underline;">未勾选 - 横向双页<br/></span>左右两页各用一个视口</p><p><span style=" font-weight:600; text-decoration: underline;">勾选 - 横向单页<br/></span>单页使用一个居中视口</p></body></html>',
})

# ---------------------------------------------------------------------------
# f-string 片段表：源文件中带插值的字符串无法按整串查表（占位符需保持活跃），
# 因此以「源码片段 → 中文片段」的形式单独维护，由应用器做主串精确替换。
# 键为源码原文（含 f 前缀与引号），值为替换后的完整字面量。
# ---------------------------------------------------------------------------
FSTRING_FRAGMENTS = {
    r"f'<b>{job_progress_number}Source:</b> '":
        r"f'<b>{job_progress_number}源文件：</b> '",
    r'f"kindlegen: {e.strerror}\n\n Re-install Rosetta/Kindle Previewer/other Intel app?\n\nPlease email Amazon to make Kindle Previewer Apple silicon native at amazon.com/kindle-help"':
        r'f"kindlegen：{e.strerror}\n\n 是否重新安装 Rosetta/Kindle Previewer/其他 Intel 应用？\n\n请发邮件给 Amazon，推动 Kindle Previewer 原生支持 Apple 芯片：amazon.com/kindle-help"',
    r"f'Editing {len(self.files)} files.'":
        r"f'正在编辑 {len(self.files)} 个文件。'",
    r"f'Processing {i}/{total}: {os.path.basename(file)}'":
        r"f'正在处理 {i}/{total}：{os.path.basename(file)}'",
    r"f'{os.path.basename(file)}: CBR is read-only'":
        r"f'{os.path.basename(file)}：CBR 为只读'",
    r'f"\n...and {len(errors) - 10} more"':
        r'f"\n……另有 {len(errors) - 10} 个"',
    r"f'Successfully updated {total} files.'":
        r"f'已成功更新 {total} 个文件。'",
    r"f'Volume count ({len(volumes)}) != file count ({fileCount})'":
        r"f'卷号数量（{len(volumes)}）与文件数量（{fileCount}）不一致'",
    # 无占位符但含插值语法或紧邻变量的片段
    r'''f"{delta.days} day(s) left"''':
        r'''f"{delta.days} 天后结束"''',
    r"f'{job_progress_number}Creating MOBI files'":
        r"f'{job_progress_number}正在生成 MOBI 文件'",
    # 拼接式消息（含 HTML 片段，无法整串查表）
    r"""'<a href="' + html_url + '"><b>The new version is available!</b></a>'""":
        r"""'<a href="' + html_url + '"><b>有新版本可用！</b></a>'""",
    r"message += ' [referral]'":
        r"message += ' [推广链接]'",
}


# ---------------------------------------------------------------------------
# 代码加固：为让中文界面正常工作所需的源码改动（与翻译表分开维护）。
# 这些替换针对上游原始写法，幂等（已加固的源码中不存在旧写法）。
# ---------------------------------------------------------------------------

# 1) 下拉框查找必须走 userData，不能用显示文字当字典键；
#    否则界面文字一旦翻译，每次查找都会 KeyError。
HARDENING_COMBO = {
    'GUI.deviceBox.currentText()': 'GUI.deviceBox.currentData()',
    'GUI.formatBox.currentText()': 'GUI.formatBox.currentData()',
}

# 2) 跨页标注对话框：改用布尔状态，不再比较标签文字
#    （上游以 label2.text() == "not a spread" 判断状态，翻译后会静默出错）
SPREAD_DIALOG_REPLACEMENTS = [
    # 初始化：建立 isSpread 状态
    ('''        label2.setText("not a spread")

        help_text = [
            "Use arrows to change index.",
            "Use space bar to confirm spreads.",
            "Use spread shift option to offset by 1.",
            "Use enter key to confirm all spreads."
            "Close window to cancel."
        ]''',
     '''        # 用独立布尔状态记录当前页是否已标记为跨页，不依赖标签文字判断
        self.isSpread = self.index2page[self.index] in self.spreads
        label2.setText('跨页' if self.isSpread else '不是跨页')

        help_text = [
            "使用方向键切换页面。",
            "按空格键确认跨页。",
            "使用跨页偏移选项可整体偏移 1 页。",
            "按回车键确认所有跨页标记。",
            "关闭窗口可取消。"
        ]'''),
    # 新增状态刷新方法（注意：上游此段含尾随空格的空行，须原样匹配）
    ('        #self.resize(pixmap2.width(), pixmap2.height())\n'
     '    \n'
     '    def keyReleaseEvent(self, event):',
     '        #self.resize(pixmap2.width(), pixmap2.height())\n'
     '\n'
     '    def _refreshSpreadState(self):\n'
     "        self.isSpread = self.index2page[self.index] in self.spreads\n"
     "        self.label2.setText('跨页' if self.isSpread else '不是跨页')\n"
     '\n'
     '    def keyReleaseEvent(self, event):'),
    # 左键：改用状态刷新
    ('''                self.index = max(0, self.index - 1)
                if self.index2page[self.index] in self.spreads:
                    self.label2.setText('spread')
                else:
                    self.label2.setText('not a spread')''',
     '''                self.index = max(0, self.index - 1)
                self._refreshSpreadState()'''),
    # 右键：改用状态刷新
    ('''                self.index = min(self.index + 1, len(self.images) - 1)
                if self.index2page[self.index] in self.spreads:
                    self.label2.setText('spread')
                else:
                    self.label2.setText('not a spread')''',
     '''                self.index = min(self.index + 1, len(self.images) - 1)
                self._refreshSpreadState()'''),
    # 空格键：用布尔状态切换，不再读标签文字
    ('''                if self.label2.text() == "not a spread":
                    self.spreads.append(os.path.basename(self.images[self.index]))
                    self.label2.setText('spread')
                else:
                    self.spreads.remove(os.path.basename(self.images[self.index]))
                    self.label2.setText('not a spread')''',
     '''                if self.isSpread:
                    self.spreads.remove(os.path.basename(self.images[self.index]))
                else:
                    self.spreads.append(os.path.basename(self.images[self.index]))
                self._refreshSpreadState()'''),
]

# 需要应用加固的源文件
HARDENING_TARGETS = {
    'combo': ['kindlecomicconverter/KCC_gui.py'],
    'spread': ['kindlecomicconverter/KCC_spread_label.py'],
}
