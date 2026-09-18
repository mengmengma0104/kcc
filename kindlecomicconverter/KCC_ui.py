# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'KCC.ui'
##
## Created by: Qt User Interface Compiler version 6.9.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QProgressBar,
    QPushButton, QSizePolicy, QSlider, QSpinBox,
    QStatusBar, QWidget)
from . import KCC_rc

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(783, 706)
        icon = QIcon()
        icon.addFile(u":/Icon/icons/comic2ebook.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        mainWindow.setWindowIcon(icon)
        self.centralWidget = QWidget(mainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.gridLayout = QGridLayout(self.centralWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 5)
        self.jobList = QListWidget(self.centralWidget)
        self.jobList.setObjectName(u"jobList")
        self.jobList.setMinimumSize(QSize(0, 90))
        self.jobList.setStyleSheet(u"")
        self.jobList.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.jobList.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.jobList.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)

        self.gridLayout.addWidget(self.jobList, 2, 0, 1, 2)

        self.croppingWidget = QWidget(self.centralWidget)
        self.croppingWidget.setObjectName(u"croppingWidget")
        self.croppingWidget.setVisible(False)
        self.gridLayout_5 = QGridLayout(self.croppingWidget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.croppingPowerSlider = QSlider(self.croppingWidget)
        self.croppingPowerSlider.setObjectName(u"croppingPowerSlider")
        self.croppingPowerSlider.setMaximum(300)
        self.croppingPowerSlider.setSingleStep(1)
        self.croppingPowerSlider.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_5.addWidget(self.croppingPowerSlider, 0, 1, 1, 1)

        self.preserveMarginBox = QSpinBox(self.croppingWidget)
        self.preserveMarginBox.setObjectName(u"preserveMarginBox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.preserveMarginBox.sizePolicy().hasHeightForWidth())
        self.preserveMarginBox.setSizePolicy(sizePolicy)
        self.preserveMarginBox.setMaximum(99)
        self.preserveMarginBox.setSingleStep(5)
        self.preserveMarginBox.setValue(0)

        self.gridLayout_5.addWidget(self.preserveMarginBox, 1, 1, 1, 1)

        self.preserveMarginLabel = QLabel(self.croppingWidget)
        self.preserveMarginLabel.setObjectName(u"preserveMarginLabel")

        self.gridLayout_5.addWidget(self.preserveMarginLabel, 1, 0, 1, 1)

        self.croppingPowerLabel = QLabel(self.croppingWidget)
        self.croppingPowerLabel.setObjectName(u"croppingPowerLabel")

        self.gridLayout_5.addWidget(self.croppingPowerLabel, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.croppingWidget, 9, 0, 1, 2)

        self.gammaWidget = QWidget(self.centralWidget)
        self.gammaWidget.setObjectName(u"gammaWidget")
        self.gammaWidget.setVisible(False)
        self.horizontalLayout_2 = QHBoxLayout(self.gammaWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gammaLabel = QLabel(self.gammaWidget)
        self.gammaLabel.setObjectName(u"gammaLabel")

        self.horizontalLayout_2.addWidget(self.gammaLabel)

        self.gammaSlider = QSlider(self.gammaWidget)
        self.gammaSlider.setObjectName(u"gammaSlider")
        self.gammaSlider.setMaximum(250)
        self.gammaSlider.setSingleStep(5)
        self.gammaSlider.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_2.addWidget(self.gammaSlider)


        self.gridLayout.addWidget(self.gammaWidget, 7, 0, 1, 2)

        self.customWidget = QWidget(self.centralWidget)
        self.customWidget.setObjectName(u"customWidget")
        self.customWidget.setVisible(False)
        self.gridLayout_3 = QGridLayout(self.customWidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.hLabel = QLabel(self.customWidget)
        self.hLabel.setObjectName(u"hLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.hLabel.sizePolicy().hasHeightForWidth())
        self.hLabel.setSizePolicy(sizePolicy1)

        self.gridLayout_3.addWidget(self.hLabel, 0, 2, 1, 1)

        self.widthBox = QSpinBox(self.customWidget)
        self.widthBox.setObjectName(u"widthBox")
        self.widthBox.setMaximum(6000)

        self.gridLayout_3.addWidget(self.widthBox, 0, 1, 1, 1)

        self.wLabel = QLabel(self.customWidget)
        self.wLabel.setObjectName(u"wLabel")
        sizePolicy1.setHeightForWidth(self.wLabel.sizePolicy().hasHeightForWidth())
        self.wLabel.setSizePolicy(sizePolicy1)

        self.gridLayout_3.addWidget(self.wLabel, 0, 0, 1, 1)

        self.heightBox = QSpinBox(self.customWidget)
        self.heightBox.setObjectName(u"heightBox")
        self.heightBox.setMaximum(8000)

        self.gridLayout_3.addWidget(self.heightBox, 0, 3, 1, 1)


        self.gridLayout.addWidget(self.customWidget, 8, 0, 1, 2)

        self.buttonWidget = QWidget(self.centralWidget)
        self.buttonWidget.setObjectName(u"buttonWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.buttonWidget.sizePolicy().hasHeightForWidth())
        self.buttonWidget.setSizePolicy(sizePolicy2)
        self.gridLayout_4 = QGridLayout(self.buttonWidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.directoryButton = QPushButton(self.buttonWidget)
        self.directoryButton.setObjectName(u"directoryButton")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.directoryButton.sizePolicy().hasHeightForWidth())
        self.directoryButton.setSizePolicy(sizePolicy3)
        icon1 = QIcon()
        icon1.addFile(u":/Other/icons/folder_new.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.directoryButton.setIcon(icon1)

        self.gridLayout_4.addWidget(self.directoryButton, 0, 4, 1, 1)

        self.formatBox = QComboBox(self.buttonWidget)
        self.formatBox.setObjectName(u"formatBox")
        self.formatBox.setMinimumSize(QSize(0, 28))

        self.gridLayout_4.addWidget(self.formatBox, 1, 4, 1, 1)

        self.deviceBox = QComboBox(self.buttonWidget)
        self.deviceBox.setObjectName(u"deviceBox")
        self.deviceBox.setMinimumSize(QSize(0, 28))

        self.gridLayout_4.addWidget(self.deviceBox, 1, 1, 1, 1)

        self.clearButton = QPushButton(self.buttonWidget)
        self.clearButton.setObjectName(u"clearButton")
        self.clearButton.setMinimumSize(QSize(0, 30))
        icon2 = QIcon()
        icon2.addFile(u":/Other/icons/clear.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.clearButton.setIcon(icon2)

        self.gridLayout_4.addWidget(self.clearButton, 0, 3, 1, 1)

        self.fileButton = QPushButton(self.buttonWidget)
        self.fileButton.setObjectName(u"fileButton")
        self.fileButton.setMinimumSize(QSize(0, 30))
        icon3 = QIcon()
        icon3.addFile(u":/Other/icons/document_new.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.fileButton.setIcon(icon3)

        self.gridLayout_4.addWidget(self.fileButton, 0, 1, 1, 1)

        self.convertButton = QPushButton(self.buttonWidget)
        self.convertButton.setObjectName(u"convertButton")
        self.convertButton.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setBold(True)
        self.convertButton.setFont(font)
        icon4 = QIcon()
        icon4.addFile(u":/Other/icons/convert.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.convertButton.setIcon(icon4)

        self.gridLayout_4.addWidget(self.convertButton, 1, 3, 1, 1)

        self.clearButton.raise_()
        self.deviceBox.raise_()
        self.convertButton.raise_()
        self.fileButton.raise_()
        self.directoryButton.raise_()
        self.formatBox.raise_()

        self.gridLayout.addWidget(self.buttonWidget, 3, 0, 1, 2)

        self.optionWidget = QWidget(self.centralWidget)
        self.optionWidget.setObjectName(u"optionWidget")
        self.gridLayout_2 = QGridLayout(self.optionWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.qualityBox = QCheckBox(self.optionWidget)
        self.qualityBox.setObjectName(u"qualityBox")
        self.qualityBox.setTristate(True)

        self.gridLayout_2.addWidget(self.qualityBox, 4, 2, 1, 1)

        self.legacyExtractBox = QCheckBox(self.optionWidget)
        self.legacyExtractBox.setObjectName(u"legacyExtractBox")

        self.gridLayout_2.addWidget(self.legacyExtractBox, 3, 1, 1, 1)

        self.outputSplit = QCheckBox(self.optionWidget)
        self.outputSplit.setObjectName(u"outputSplit")

        self.gridLayout_2.addWidget(self.outputSplit, 4, 1, 1, 1)

        self.tempDirBox = QCheckBox(self.optionWidget)
        self.tempDirBox.setObjectName(u"tempDirBox")

        self.gridLayout_2.addWidget(self.tempDirBox, 10, 2, 1, 1)

        self.disableProcessingBox = QCheckBox(self.optionWidget)
        self.disableProcessingBox.setObjectName(u"disableProcessingBox")

        self.gridLayout_2.addWidget(self.disableProcessingBox, 6, 3, 1, 1)

        self.upscaleBox = QCheckBox(self.optionWidget)
        self.upscaleBox.setObjectName(u"upscaleBox")
        self.upscaleBox.setTristate(True)

        self.gridLayout_2.addWidget(self.upscaleBox, 2, 1, 1, 1)

        self.interPanelCropBox = QCheckBox(self.optionWidget)
        self.interPanelCropBox.setObjectName(u"interPanelCropBox")
        self.interPanelCropBox.setTristate(True)

        self.gridLayout_2.addWidget(self.interPanelCropBox, 6, 2, 1, 1)

        self.languageEdit = QLineEdit(self.optionWidget)
        self.languageEdit.setObjectName(u"languageEdit")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.languageEdit.sizePolicy().hasHeightForWidth())
        self.languageEdit.setSizePolicy(sizePolicy4)
        self.languageEdit.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.languageEdit.setClearButtonEnabled(False)

        self.gridLayout_2.addWidget(self.languageEdit, 0, 3, 1, 1)

        self.webtoonBox = QCheckBox(self.optionWidget)
        self.webtoonBox.setObjectName(u"webtoonBox")

        self.gridLayout_2.addWidget(self.webtoonBox, 2, 0, 1, 1)

        self.noRotateBox = QCheckBox(self.optionWidget)
        self.noRotateBox.setObjectName(u"noRotateBox")

        self.gridLayout_2.addWidget(self.noRotateBox, 6, 1, 1, 1)

        self.deleteBox = QCheckBox(self.optionWidget)
        self.deleteBox.setObjectName(u"deleteBox")

        self.gridLayout_2.addWidget(self.deleteBox, 1, 3, 1, 1)

        self.invertDirectionBox = QCheckBox(self.optionWidget)
        self.invertDirectionBox.setObjectName(u"invertDirectionBox")

        self.gridLayout_2.addWidget(self.invertDirectionBox, 9, 3, 1, 1)

        self.noQuantizeBox = QCheckBox(self.optionWidget)
        self.noQuantizeBox.setObjectName(u"noQuantizeBox")
        self.noQuantizeBox.setEnabled(False)

        self.gridLayout_2.addWidget(self.noQuantizeBox, 7, 3, 1, 1)

        self.rotateFirstBox = QCheckBox(self.optionWidget)
        self.rotateFirstBox.setObjectName(u"rotateFirstBox")

        self.gridLayout_2.addWidget(self.rotateFirstBox, 7, 1, 1, 1)

        self.croppingBox = QCheckBox(self.optionWidget)
        self.croppingBox.setObjectName(u"croppingBox")
        self.croppingBox.setTristate(True)

        self.gridLayout_2.addWidget(self.croppingBox, 1, 2, 1, 1)

        self.authorEdit = QLineEdit(self.optionWidget)
        self.authorEdit.setObjectName(u"authorEdit")
        sizePolicy4.setHeightForWidth(self.authorEdit.sizePolicy().hasHeightForWidth())
        self.authorEdit.setSizePolicy(sizePolicy4)
        self.authorEdit.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.authorEdit.setClearButtonEnabled(False)

        self.gridLayout_2.addWidget(self.authorEdit, 0, 1, 1, 1)

        self.mozJpegBox = QCheckBox(self.optionWidget)
        self.mozJpegBox.setObjectName(u"mozJpegBox")
        self.mozJpegBox.setTristate(True)

        self.gridLayout_2.addWidget(self.mozJpegBox, 4, 0, 1, 1)

        self.lightnovelBox = QCheckBox(self.optionWidget)
        self.lightnovelBox.setObjectName(u"lightnovelBox")

        self.gridLayout_2.addWidget(self.lightnovelBox, 10, 0, 1, 1)

        self.metadataTitleBox = QCheckBox(self.optionWidget)
        self.metadataTitleBox.setObjectName(u"metadataTitleBox")
        self.metadataTitleBox.setTristate(True)

        self.gridLayout_2.addWidget(self.metadataTitleBox, 2, 3, 1, 1)

        self.fileFusionBox = QCheckBox(self.optionWidget)
        self.fileFusionBox.setObjectName(u"fileFusionBox")

        self.gridLayout_2.addWidget(self.fileFusionBox, 6, 0, 1, 1)

        self.forcePngRgbBox = QCheckBox(self.optionWidget)
        self.forcePngRgbBox.setObjectName(u"forcePngRgbBox")
        self.forcePngRgbBox.setEnabled(False)

        self.gridLayout_2.addWidget(self.forcePngRgbBox, 8, 3, 1, 1)

        self.wallpaperBox = QCheckBox(self.optionWidget)
        self.wallpaperBox.setObjectName(u"wallpaperBox")

        self.gridLayout_2.addWidget(self.wallpaperBox, 11, 0, 1, 1)

        self.maximizeStrips = QCheckBox(self.optionWidget)
        self.maximizeStrips.setObjectName(u"maximizeStrips")

        self.gridLayout_2.addWidget(self.maximizeStrips, 5, 1, 1, 1)

        self.autoLevelBox = QCheckBox(self.optionWidget)
        self.autoLevelBox.setObjectName(u"autoLevelBox")

        self.gridLayout_2.addWidget(self.autoLevelBox, 7, 2, 1, 1)

        self.ebokBox = QCheckBox(self.optionWidget)
        self.ebokBox.setObjectName(u"ebokBox")

        self.gridLayout_2.addWidget(self.ebokBox, 10, 3, 1, 1)

        self.pdfWidthBox = QCheckBox(self.optionWidget)
        self.pdfWidthBox.setObjectName(u"pdfWidthBox")

        self.gridLayout_2.addWidget(self.pdfWidthBox, 4, 3, 1, 1)

        self.autocontrastBox = QCheckBox(self.optionWidget)
        self.autocontrastBox.setObjectName(u"autocontrastBox")
        self.autocontrastBox.setTristate(True)

        self.gridLayout_2.addWidget(self.autocontrastBox, 8, 2, 1, 1)

        self.outputFolderWidget = QWidget(self.optionWidget)
        self.outputFolderWidget.setObjectName(u"outputFolderWidget")
        self.horizontalLayout_3 = QHBoxLayout(self.outputFolderWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.defaultOutputFolderBox = QCheckBox(self.outputFolderWidget)
        self.defaultOutputFolderBox.setObjectName(u"defaultOutputFolderBox")
        sizePolicy.setHeightForWidth(self.defaultOutputFolderBox.sizePolicy().hasHeightForWidth())
        self.defaultOutputFolderBox.setSizePolicy(sizePolicy)
        self.defaultOutputFolderBox.setTristate(True)

        self.horizontalLayout_3.addWidget(self.defaultOutputFolderBox)

        self.defaultOutputFolderButton = QPushButton(self.outputFolderWidget)
        self.defaultOutputFolderButton.setObjectName(u"defaultOutputFolderButton")
        self.defaultOutputFolderButton.setMinimumSize(QSize(0, 30))
        self.defaultOutputFolderButton.setIcon(icon1)

        self.horizontalLayout_3.addWidget(self.defaultOutputFolderButton)


        self.gridLayout_2.addWidget(self.outputFolderWidget, 0, 2, 1, 1)

        self.pngLegacyBox = QCheckBox(self.optionWidget)
        self.pngLegacyBox.setObjectName(u"pngLegacyBox")
        self.pngLegacyBox.setEnabled(False)

        self.gridLayout_2.addWidget(self.pngLegacyBox, 8, 0, 1, 1)

        self.rotateRightBox = QCheckBox(self.optionWidget)
        self.rotateRightBox.setObjectName(u"rotateRightBox")

        self.gridLayout_2.addWidget(self.rotateRightBox, 9, 1, 1, 1)

        self.vertical4PanelBox = QCheckBox(self.optionWidget)
        self.vertical4PanelBox.setObjectName(u"vertical4PanelBox")

        self.gridLayout_2.addWidget(self.vertical4PanelBox, 9, 2, 1, 1)

        self.borderBox = QCheckBox(self.optionWidget)
        self.borderBox.setObjectName(u"borderBox")
        self.borderBox.setTristate(True)

        self.gridLayout_2.addWidget(self.borderBox, 3, 0, 1, 1)

        self.eraseRainbowBox = QCheckBox(self.optionWidget)
        self.eraseRainbowBox.setObjectName(u"eraseRainbowBox")

        self.gridLayout_2.addWidget(self.eraseRainbowBox, 3, 2, 1, 1)

        self.webpBox = QCheckBox(self.optionWidget)
        self.webpBox.setObjectName(u"webpBox")

        self.gridLayout_2.addWidget(self.webpBox, 9, 0, 1, 1)

        self.rotateBox = QCheckBox(self.optionWidget)
        self.rotateBox.setObjectName(u"rotateBox")
        self.rotateBox.setTristate(True)

        self.gridLayout_2.addWidget(self.rotateBox, 1, 1, 1, 1)

        self.chunkSizeCheckBox = QCheckBox(self.optionWidget)
        self.chunkSizeCheckBox.setObjectName(u"chunkSizeCheckBox")

        self.gridLayout_2.addWidget(self.chunkSizeCheckBox, 5, 3, 1, 1)

        self.jpegQualityBox = QCheckBox(self.optionWidget)
        self.jpegQualityBox.setObjectName(u"jpegQualityBox")

        self.gridLayout_2.addWidget(self.jpegQualityBox, 7, 0, 1, 1)

        self.gammaBox = QCheckBox(self.optionWidget)
        self.gammaBox.setObjectName(u"gammaBox")

        self.gridLayout_2.addWidget(self.gammaBox, 5, 2, 1, 1)

        self.mangaBox = QCheckBox(self.optionWidget)
        self.mangaBox.setObjectName(u"mangaBox")

        self.gridLayout_2.addWidget(self.mangaBox, 1, 0, 1, 1)

        self.colorBox = QCheckBox(self.optionWidget)
        self.colorBox.setObjectName(u"colorBox")

        self.gridLayout_2.addWidget(self.colorBox, 2, 2, 1, 1)

        self.titleEdit = QLineEdit(self.optionWidget)
        self.titleEdit.setObjectName(u"titleEdit")
        sizePolicy4.setHeightForWidth(self.titleEdit.sizePolicy().hasHeightForWidth())
        self.titleEdit.setSizePolicy(sizePolicy4)
        self.titleEdit.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.titleEdit.setClearButtonEnabled(False)

        self.gridLayout_2.addWidget(self.titleEdit, 0, 0, 1, 1)

        self.coverFillBox = QCheckBox(self.optionWidget)
        self.coverFillBox.setObjectName(u"coverFillBox")

        self.gridLayout_2.addWidget(self.coverFillBox, 8, 1, 1, 1)

        self.smartCoverCropBox = QCheckBox(self.optionWidget)
        self.smartCoverCropBox.setObjectName(u"smartCoverCropBox")

        self.gridLayout_2.addWidget(self.smartCoverCropBox, 10, 1, 1, 1)

        self.spreadShiftBox = QCheckBox(self.optionWidget)
        self.spreadShiftBox.setObjectName(u"spreadShiftBox")

        self.gridLayout_2.addWidget(self.spreadShiftBox, 5, 0, 1, 1)

        self.onePageLandscapeBox = QCheckBox(self.optionWidget)
        self.onePageLandscapeBox.setObjectName(u"onePageLandscapeBox")

        self.gridLayout_2.addWidget(self.onePageLandscapeBox, 11, 1, 1, 1)

        self.keepComicInfoBox = QCheckBox(self.optionWidget)
        self.keepComicInfoBox.setObjectName(u"keepComicInfoBox")

        self.gridLayout_2.addWidget(self.keepComicInfoBox, 3, 3, 1, 1)


        self.gridLayout.addWidget(self.optionWidget, 5, 0, 1, 2)

        self.jpegQualityWidget = QWidget(self.centralWidget)
        self.jpegQualityWidget.setObjectName(u"jpegQualityWidget")
        sizePolicy1.setHeightForWidth(self.jpegQualityWidget.sizePolicy().hasHeightForWidth())
        self.jpegQualityWidget.setSizePolicy(sizePolicy1)
        self.jpegQualityWidget.setVisible(False)
        self.horizontalLayout_12 = QHBoxLayout(self.jpegQualityWidget)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.jpegQualityLabel = QLabel(self.jpegQualityWidget)
        self.jpegQualityLabel.setObjectName(u"jpegQualityLabel")

        self.horizontalLayout_12.addWidget(self.jpegQualityLabel)

        self.jpegQualitySpinBox = QSpinBox(self.jpegQualityWidget)
        self.jpegQualitySpinBox.setObjectName(u"jpegQualitySpinBox")
        self.jpegQualitySpinBox.setMaximum(95)
        self.jpegQualitySpinBox.setSingleStep(5)
        self.jpegQualitySpinBox.setValue(85)

        self.horizontalLayout_12.addWidget(self.jpegQualitySpinBox)


        self.gridLayout.addWidget(self.jpegQualityWidget, 10, 0, 1, 1)

        self.toolWidget = QWidget(self.centralWidget)
        self.toolWidget.setObjectName(u"toolWidget")
        self.gridLayout_6 = QGridLayout(self.toolWidget)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.labelSpreadsButton = QPushButton(self.toolWidget)
        self.labelSpreadsButton.setObjectName(u"labelSpreadsButton")
        self.labelSpreadsButton.setMinimumSize(QSize(0, 30))

        self.gridLayout_6.addWidget(self.labelSpreadsButton, 0, 1, 1, 1)

        self.kofiButton = QPushButton(self.toolWidget)
        self.kofiButton.setObjectName(u"kofiButton")
        self.kofiButton.setMinimumSize(QSize(0, 30))
        icon5 = QIcon()
        icon5.addFile(u":/Brand/icons/kofi_symbol.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.kofiButton.setIcon(icon5)
        self.kofiButton.setIconSize(QSize(19, 16))

        self.gridLayout_6.addWidget(self.kofiButton, 0, 2, 1, 1)

        self.editorButton = QPushButton(self.toolWidget)
        self.editorButton.setObjectName(u"editorButton")
        self.editorButton.setMinimumSize(QSize(0, 30))
        icon6 = QIcon()
        icon6.addFile(u":/Other/icons/editor.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.editorButton.setIcon(icon6)

        self.gridLayout_6.addWidget(self.editorButton, 0, 0, 1, 1)

        self.humbleButton = QPushButton(self.toolWidget)
        self.humbleButton.setObjectName(u"humbleButton")
        self.humbleButton.setMinimumSize(QSize(0, 30))
        icon7 = QIcon()
        icon7.addFile(u":/Brand/icons/Humble_H-Red.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.humbleButton.setIcon(icon7)

        self.gridLayout_6.addWidget(self.humbleButton, 0, 3, 1, 1)

        self.expertButton = QPushButton(self.toolWidget)
        self.expertButton.setObjectName(u"expertButton")
        self.expertButton.setMinimumSize(QSize(0, 30))

        self.gridLayout_6.addWidget(self.expertButton, 0, 4, 1, 1)


        self.gridLayout.addWidget(self.toolWidget, 0, 0, 1, 2)

        self.chunkSizeWidget = QWidget(self.centralWidget)
        self.chunkSizeWidget.setObjectName(u"chunkSizeWidget")
        sizePolicy4.setHeightForWidth(self.chunkSizeWidget.sizePolicy().hasHeightForWidth())
        self.chunkSizeWidget.setSizePolicy(sizePolicy4)
        self.chunkSizeWidget.setVisible(False)
        self.horizontalLayout_4 = QHBoxLayout(self.chunkSizeWidget)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.chunkSizeLabel = QLabel(self.chunkSizeWidget)
        self.chunkSizeLabel.setObjectName(u"chunkSizeLabel")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.chunkSizeLabel.sizePolicy().hasHeightForWidth())
        self.chunkSizeLabel.setSizePolicy(sizePolicy5)

        self.horizontalLayout_4.addWidget(self.chunkSizeLabel)

        self.chunkSizeBox = QSpinBox(self.chunkSizeWidget)
        self.chunkSizeBox.setObjectName(u"chunkSizeBox")
        self.chunkSizeBox.setMinimum(50)
        self.chunkSizeBox.setMaximum(600)
        self.chunkSizeBox.setValue(400)

        self.horizontalLayout_4.addWidget(self.chunkSizeBox)

        self.chunkSizeWarnLabel = QLabel(self.chunkSizeWidget)
        self.chunkSizeWarnLabel.setObjectName(u"chunkSizeWarnLabel")
        sizePolicy5.setHeightForWidth(self.chunkSizeWarnLabel.sizePolicy().hasHeightForWidth())
        self.chunkSizeWarnLabel.setSizePolicy(sizePolicy5)

        self.horizontalLayout_4.addWidget(self.chunkSizeWarnLabel)


        self.gridLayout.addWidget(self.chunkSizeWidget, 6, 0, 1, 1)

        self.progressBar = QProgressBar(self.centralWidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(0, 30))
        self.progressBar.setFont(font)
        self.progressBar.setVisible(False)
        self.progressBar.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.progressBar, 1, 0, 1, 2)

        self.easyLabel = QLabel(self.centralWidget)
        self.easyLabel.setObjectName(u"easyLabel")
        self.easyLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.easyLabel, 4, 0, 1, 2)

        mainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QStatusBar(mainWindow)
        self.statusBar.setObjectName(u"statusBar")
        self.statusBar.setSizeGripEnabled(False)
        mainWindow.setStatusBar(self.statusBar)
        QWidget.setTabOrder(self.jobList, self.fileButton)
        QWidget.setTabOrder(self.fileButton, self.clearButton)
        QWidget.setTabOrder(self.clearButton, self.deviceBox)
        QWidget.setTabOrder(self.deviceBox, self.widthBox)
        QWidget.setTabOrder(self.widthBox, self.heightBox)
        QWidget.setTabOrder(self.heightBox, self.convertButton)
        QWidget.setTabOrder(self.convertButton, self.mangaBox)
        QWidget.setTabOrder(self.mangaBox, self.rotateBox)
        QWidget.setTabOrder(self.rotateBox, self.webtoonBox)
        QWidget.setTabOrder(self.webtoonBox, self.upscaleBox)
        QWidget.setTabOrder(self.upscaleBox, self.gammaSlider)
        QWidget.setTabOrder(self.gammaSlider, self.borderBox)
        QWidget.setTabOrder(self.borderBox, self.mozJpegBox)
        QWidget.setTabOrder(self.mozJpegBox, self.croppingPowerSlider)
        QWidget.setTabOrder(self.croppingPowerSlider, self.preserveMarginBox)
        QWidget.setTabOrder(self.preserveMarginBox, self.spreadShiftBox)
        QWidget.setTabOrder(self.spreadShiftBox, self.fileFusionBox)
        QWidget.setTabOrder(self.fileFusionBox, self.chunkSizeBox)
        QWidget.setTabOrder(self.chunkSizeBox, self.editorButton)
        QWidget.setTabOrder(self.editorButton, self.kofiButton)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"Kindle 漫画转换器", None))
#if QT_CONFIG(tooltip)
        self.jobList.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>双击列表中的文件，可在元数据编辑器中打开。</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.preserveMarginLabel.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>计算裁剪边界后，按指定百分比向外“回退”留白。</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.preserveMarginLabel.setText(QCoreApplication.translate("mainWindow", u"保留边距 %", None))
        self.croppingPowerLabel.setText(QCoreApplication.translate("mainWindow", u"裁剪力度：", None))
        self.gammaLabel.setText(QCoreApplication.translate("mainWindow", u"伽马：自动", None))
#if QT_CONFIG(tooltip)
        self.hLabel.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p style='white-space:pre'>目标设备的分辨率。</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.hLabel.setText(QCoreApplication.translate("mainWindow", u"自定义高度：", None))
#if QT_CONFIG(tooltip)
        self.widthBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p style='white-space:pre'>目标设备的分辨率。</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.wLabel.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p style='white-space:pre'>目标设备的分辨率。</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.wLabel.setText(QCoreApplication.translate("mainWindow", u"自定义宽度：", None))
#if QT_CONFIG(tooltip)
        self.heightBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p style='white-space:pre'>目标设备的分辨率。</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.directoryButton.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p style='white-space:pre'>把包含 JPG、PNG 或 GIF 文件的目录加入队列。<br/><span style=\" font-weight:600;\">目录内的 CBR、CBZ 和 CB7 文件不会被处理！</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.directoryButton.setText(QCoreApplication.translate("mainWindow", u"添加输入文件夹", None))
#if QT_CONFIG(tooltip)
        self.formatBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p style='white-space:pre'>输出格式。</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.deviceBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p style='white-space:pre'>目标设备。</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.clearButton.setText(QCoreApplication.translate("mainWindow", u"清空列表", None))
#if QT_CONFIG(tooltip)
        self.fileButton.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p style='white-space:pre'>把 CBR、CBZ、CB7 或 PDF 文件加入队列。</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.fileButton.setText(QCoreApplication.translate("mainWindow", u"添加输入文件", None))
#if QT_CONFIG(tooltip)
        self.convertButton.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p style='white-space:pre'>按住 Shift 点击，可为该列表单独指定输出目录。</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.convertButton.setText(QCoreApplication.translate("mainWindow", u"开始转换", None))
#if QT_CONFIG(tooltip)
        self.qualityBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p style='white-space:pre'><span style=\" font-weight:600; text-decoration: underline;\">未勾选 - 4 面板<br/></span>分别放大四个角。</p><p style='white-space:pre'><span style=\" font-weight:600; text-decoration: underline;\">半选 - 2 面板<br/></span>只放大页面的顶部和底部。</p><p><span style=\" font-weight:600; text-decoration: underline;\">勾选 - 4 个高质量面板<br/></span>分别放大四个角，并尽量提高放大质量。详见 wiki。</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.qualityBox.setText(QCoreApplication.translate("mainWindow", u"面板视图 4/2/高质量", None))
#if QT_CONFIG(tooltip)
        self.legacyExtractBox.setToolTip(QCoreApplication.translate("mainWindow", u"使用旧版 KCC 的 PDF/EPUB 图片提取方式。\n\n标准提取方式因故失败时可尝试此项。", None))
#endif // QT_CONFIG(tooltip)
        self.legacyExtractBox.setText(QCoreApplication.translate("mainWindow", u"旧版提取方式", None))
#if QT_CONFIG(tooltip)
        self.outputSplit.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p style='white-space:pre'><span style=\" font-weight:600; text-decoration: underline;\">未勾选 - 自动模式<br/></span>输出文件会自动分卷。</p><p style='white-space:pre'><span style=\" font-weight:600; text-decoration: underline;\">勾选 - 分卷模式<br/></span>每个子目录视为独立的一卷。</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.outputSplit.setText(QCoreApplication.translate("mainWindow", u"输出分卷", None))
#if QT_CONFIG(tooltip)
        self.tempDirBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">未勾选 - 主硬盘<br/></span>在系统主硬盘上使用专用临时目录。</p><p><span style=\" font-weight:600; text-decoration: underline;\">勾选 - 源文件所在盘<br/></span>在源文件所在磁盘创建临时目录。</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.tempDirBox.setText(QCoreApplication.translate("mainWindow", u"临时目录", None))
#if QT_CONFIG(tooltip)
        self.disableProcessingBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p style='white-space:pre'>不对图像做任何处理，忽略配置文件和图像处理选项。</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.disableProcessingBox.setText(QCoreApplication.translate("mainWindow", u"禁用图像处理", None))
#if QT_CONFIG(tooltip)
        self.upscaleBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">未勾选 - 不处理<br/></span>小于设备分辨率的图像不缩放。</p><p><span style=\" font-weight:600; text-decoration: underline;\">半选 - 拉伸<br/></span>小于设备分辨率的图像会被缩放，不保持宽高比。</p><p><span style=\" font-weight:600; text-decoration: underline;\">勾选 - 放大<br/></span>小于设备分辨率的图像会被缩放，并保持宽高比。</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.upscaleBox.setText(QCoreApplication.translate("mainWindow", u"拉伸/放大", None))
#if QT_CONFIG(tooltip)
        self.interPanelCropBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">未勾选 - 禁用<br/></span>禁用</p><p><span style=\" font-weight:600; text-decoration: underline;\">半选 - 横向<br/></span>裁掉空白横向条带。</p><p><span style=\" font-weight:600; text-decoration: underline;\">勾选 - 双向<br/></span>裁掉空白横向和纵向条带。</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.interPanelCropBox.setText(QCoreApplication.translate("mainWindow", u"面板间裁剪", None))
#if QT_CONFIG(tooltip)
        self.languageEdit.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>默认 EPUB 语言为 en-US。</p><p>仅在您的 EPUB 阅读器对英文字体有问题时才需要修改。</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.languageEdit.setPlaceholderText(QCoreApplication.translate("mainWindow", u"EPUB 语言", None))
#if QT_CONFIG(tooltip)
        self.webtoonBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p style='white-space:pre'>启用韩式条漫的特殊解析模式。</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.webtoonBox.setText(QCoreApplication.translate("mainWindow", u"条漫模式", None))
#if QT_CONFIG(tooltip)
        self.noRotateBox.setToolTip(QCoreApplication.translate("mainWindow", u"在跨页拆分选项中不旋转跨页图。", None))
#endif // QT_CONFIG(tooltip)
        self.noRotateBox.setText(QCoreApplication.translate("mainWindow", u"不旋转", None))
#if QT_CONFIG(tooltip)
        self.deleteBox.setToolTip(QCoreApplication.translate("mainWindow", u"删除输入文件或目录。此操作不可恢复！", None))
#endif // QT_CONFIG(tooltip)
        self.deleteBox.setText(QCoreApplication.translate("mainWindow", u"删除源文件", None))
#if QT_CONFIG(tooltip)
        self.invertDirectionBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>反转翻页方向。</p><p>通常用于从右到左的漫画，但您希望从左到右翻页的情况。此时跨页拆分仍按从右到左处理。</p><p>会破坏横向模式顺序等功能。</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.invertDirectionBox.setText(QCoreApplication.translate("mainWindow", u"反转翻页方向", None))
#if QT_CONFIG(tooltip)
        self.noQuantizeBox.setToolTip(QCoreApplication.translate("mainWindow", u"不把 PNG 图像量化为 16 色（4 位）\n\n这会使文件体积翻倍，但保留全部 256 色（8 位）。\n\n电子墨水屏只有 16 级灰阶，通常不建议开启。", None))
#endif // QT_CONFIG(tooltip)
        self.noQuantizeBox.setText(QCoreApplication.translate("mainWindow", u"不做色彩量化", None))
#if QT_CONFIG(tooltip)
        self.rotateFirstBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>当“跨页拆分”为半选状态时：</p><p><span style=\" font-weight:600; text-decoration: underline;\">未勾选 - 旋转页在后<br/></span>旋转后的跨页图排在拆分页之后。</p><p><span style=\" font-weight:600; text-decoration: underline;\">勾选 - 旋转页在前<br/></span>旋转后的跨页图排在拆分页之前。</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.rotateFirstBox.setText(QCoreApplication.translate("mainWindow", u"旋转页优先", None))
#if QT_CONFIG(tooltip)
        self.croppingBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">未勾选 - 禁用</span></p><p>禁用</p><p><span style=\" font-weight:600; text-decoration: underline;\">半选 - 裁边距<br/></span>只裁边距</p><p><span style=\" font-weight:600; text-decoration: underline;\">勾选 - 边距 + 页码<br/></span>边距和页码一起裁掉</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.croppingBox.setText(QCoreApplication.translate("mainWindow", u"裁剪模式", None))
#if QT_CONFIG(tooltip)
        self.authorEdit.setToolTip(QCoreApplication.translate("mainWindow", u"默认作者为 KCC", None))
#endif // QT_CONFIG(tooltip)
        self.authorEdit.setPlaceholderText(QCoreApplication.translate("mainWindow", u"默认作者", None))
#if QT_CONFIG(tooltip)
        self.mozJpegBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">未勾选 - JPEG<br/></span>使用 JPEG 文件</p><p><span style=\" font-weight:600; text-decoration: underline;\">半选 - 强制 PNG<br/></span>黑白图像使用 PNG 而非 JPEG</p><p><span style=\" font-weight:600; text-decoration: underline;\">勾选 - mozJpeg<br/></span>画质不变，JPEG 体积小 10-20%，但处理时间翻倍</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.mozJpegBox.setText(QCoreApplication.translate("mainWindow", u"JPEG/PNG/mozJpeg", None))
#if QT_CONFIG(tooltip)
        self.lightnovelBox.setToolTip(QCoreApplication.translate("mainWindow", u"仅缩放图像并保留原始文件结构。\n\n除 JPEG 质量、彩色模式、输出文件夹外，忽略大部分选项。", None))
#endif // QT_CONFIG(tooltip)
        self.lightnovelBox.setText(QCoreApplication.translate("mainWindow", u"轻小说模式", None))
#if QT_CONFIG(tooltip)
        self.metadataTitleBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">未勾选 - 不使用元数据标题<br/></span>写入默认标题。</p><p><span style=\" font-weight:600; text-decoration: underline;\">半选 - 元数据标题追加到默认命名后<br/></span>默认标题后附加 ComicInfo.xml 等内嵌元数据中的标题。</p><p><span style=\" font-weight:600; text-decoration: underline;\">勾选 - 仅使用元数据标题<br/></span>仅使用 ComicInfo.xml 等内嵌元数据中的标题。</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.metadataTitleBox.setText(QCoreApplication.translate("mainWindow", u"元数据标题", None))
#if QT_CONFIG(tooltip)
        self.fileFusionBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>把所有选中文件合并为单个文件（便于把多个章节合并成卷）。</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.fileFusionBox.setText(QCoreApplication.translate("mainWindow", u"文件合并", None))
#if QT_CONFIG(tooltip)
        self.forcePngRgbBox.setToolTip(QCoreApplication.translate("mainWindow", u"强制把全彩图像保存为无损 PNG，文件体积会大幅增加。", None))
#endif // QT_CONFIG(tooltip)
        self.forcePngRgbBox.setText(QCoreApplication.translate("mainWindow", u"强制 PNG RGB", None))
#if QT_CONFIG(tooltip)
        self.wallpaperBox.setToolTip(QCoreApplication.translate("mainWindow", u"自动勾选专为 KOreader 壁纸设计的各类选项。\n\n同时会裁剪图像以居中铺满屏幕。", None))
#endif // QT_CONFIG(tooltip)
        self.wallpaperBox.setText(QCoreApplication.translate("mainWindow", u"壁纸模式", None))
#if QT_CONFIG(tooltip)
        self.maximizeStrips.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">未勾选 - 1x4<br/></span>保持 1x4 面板条带。</p><p><span style=\" font-weight:600; text-decoration: underline;\">勾选 - 2x2<br/></span>把 1x4 条带改为 2x2，充分利用屏幕。</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeStrips.setText(QCoreApplication.translate("mainWindow", u"1x4 转 2x2 条带", None))
#if QT_CONFIG(tooltip)
        self.autoLevelBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>默认情况下，KCC 把最暗的像素值映射为纯黑（黑点）。</p><p>“极值黑点”改为把最常见的暗像素值设为黑点。</p><p>适用于文字为黑、画面偏灰的情况。</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.autoLevelBox.setText(QCoreApplication.translate("mainWindow", u"极值黑点", None))
#if QT_CONFIG(tooltip)
        self.ebokBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>强制把 Kindle MOBI 标记为 EBOK 而不是 PDOC。</p><p>若离线超过一个月后再联网，可能导致通过 USB 导入的书籍被删除。</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.ebokBox.setText(QCoreApplication.translate("mainWindow", u"强制 EBOK", None))
#if QT_CONFIG(tooltip)
        self.pdfWidthBox.setToolTip(QCoreApplication.translate("mainWindow", u"按设备宽度而非高度渲染矢量 PDF。\n\n如果打算裁掉上下少量边缘以填满屏幕，此选项很有用。", None))
#endif // QT_CONFIG(tooltip)
        self.pdfWidthBox.setText(QCoreApplication.translate("mainWindow", u"PDF 按宽度渲染", None))
#if QT_CONFIG(tooltip)
        self.autocontrastBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">未勾选 - 仅黑白<br/></span>只对黑白页面做自动对比度。页面中不存在接近纯黑或纯白的像素时跳过。</p><p><span style=\" font-weight:600; text-decoration: underline;\">半选 - 禁用<br/></span>禁用自动对比度</p><p><span style=\" font-weight:600; text-decoration: underline;\">勾选 - 黑白与彩色<br/></span>黑白和彩色图像都做自动对比度。页面中不存在接近纯黑或纯白的像素时跳过。</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.autocontrastBox.setText(QCoreApplication.translate("mainWindow", u"自定义自动对比度", None))
#if QT_CONFIG(tooltip)
        self.defaultOutputFolderBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">未勾选 - 与源文件同目录<br/></span>输出文件放在源文件旁边</p><p><span style=\" font-weight:600; text-decoration: underline;\">半选 - 源文件旁的文件夹<br/></span>输出文件放在源文件旁的文件夹中</p><p><span style=\" font-weight:600; text-decoration: underline;\">勾选 - 自定义<br/></span>输出文件放在右侧按钮指定的自定义目录中</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.defaultOutputFolderBox.setText(QCoreApplication.translate("mainWindow", u"输出文件夹", None))
#if QT_CONFIG(tooltip)
        self.defaultOutputFolderButton.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>用于选择默认输出目录。</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.defaultOutputFolderButton.setText("")
#if QT_CONFIG(tooltip)
        self.pngLegacyBox.setToolTip(QCoreApplication.translate("mainWindow", u"使用兼容性更好的 8 位 PNG，而不是 4 位。", None))
#endif // QT_CONFIG(tooltip)
        self.pngLegacyBox.setText(QCoreApplication.translate("mainWindow", u"PNG 兼容模式", None))
#if QT_CONFIG(tooltip)
        self.rotateRightBox.setToolTip(QCoreApplication.translate("mainWindow", u"跨页图按相反方向旋转。", None))
#endif // QT_CONFIG(tooltip)
        self.rotateRightBox.setText(QCoreApplication.translate("mainWindow", u"向右旋转", None))
#if QT_CONFIG(tooltip)
        self.vertical4PanelBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>在虚拟面板模式下：</p><p><span style=\" font-weight:600; text-decoration: underline;\">未勾选 - 横向<br/></span>前两个面板是顶部面板。</p><p><span style=\" font-weight:600; text-decoration: underline;\">勾选 - 纵向<br/></span>前两个面板是侧边面板。</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.vertical4PanelBox.setText(QCoreApplication.translate("mainWindow", u"垂直四面板", None))
#if QT_CONFIG(tooltip)
        self.borderBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">未勾选 - 自动检测<br/></span>自动检测边距填充颜色。</p><p><span style=\" font-weight:600; text-decoration: underline;\">半选 - 白色<br/></span>边距保持原样。</p><p><span style=\" font-weight:600; text-decoration: underline;\">勾选 - 黑色<br/></span>边距填充为黑色。</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.borderBox.setText(QCoreApplication.translate("mainWindow", u"黑白边距", None))
#if QT_CONFIG(tooltip)
        self.eraseRainbowBox.setToolTip(QCoreApplication.translate("mainWindow", u"通过衰减干扰频率，消除彩色电子墨水屏的彩虹纹", None))
#endif // QT_CONFIG(tooltip)
        self.eraseRainbowBox.setText(QCoreApplication.translate("mainWindow", u"彩虹纹消除", None))
#if QT_CONFIG(tooltip)
        self.webpBox.setToolTip(QCoreApplication.translate("mainWindow", u"用有损 WebP 替换 JPG、用无损 WebP 替换 PNG（JPEG 质量设置同样生效）。\n\n对 Kindle 的 EPUB/MOBI 以及所有 PDF 无效。", None))
#endif // QT_CONFIG(tooltip)
        self.webpBox.setText(QCoreApplication.translate("mainWindow", u"WebP（实验性）", None))
#if QT_CONFIG(tooltip)
        self.rotateBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">未勾选 - 拆分<br/></span>跨页图裁成两个独立页面。</p><p><span style=\" font-weight:600; text-decoration: underline;\">半选 - 拆分并旋转<br/></span>跨页图显示两次：先拆分，再旋转。</p><p><span style=\" font-weight:600; text-decoration: underline;\">勾选 - 旋转<br/></span>跨页图旋转显示。</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.rotateBox.setText(QCoreApplication.translate("mainWindow", u"跨页拆分", None))
#if QT_CONFIG(tooltip)
        self.chunkSizeCheckBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p><span style=\" font-weight:700; text-decoration: underline;\">未勾选<br/></span>分卷前的最大输出体积：条漫 100 MB，其他 400 MB。</p><p><span style=\" font-weight:700; text-decoration: underline;\">勾选</span><br/>分卷前按“分块大小 MB”中指定的体积执行。</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.chunkSizeCheckBox.setText(QCoreApplication.translate("mainWindow", u"分块大小", None))
#if QT_CONFIG(tooltip)
        self.jpegQualityBox.setToolTip(QCoreApplication.translate("mainWindow", u"JPEG 质量，范围 0（最差）到 95（最好）。\n\n除 Kindle Scribe 和 Colorsoft（默认 90）外，多数设备默认 85。\n\n数值越高体积越大、质量越好，也可能解决空白页问题。", None))
#endif // QT_CONFIG(tooltip)
        self.jpegQualityBox.setText(QCoreApplication.translate("mainWindow", u"自定义 JPEG 质量", None))
#if QT_CONFIG(tooltip)
        self.gammaBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>设置自定义伽马校正。</p><p>默认 1.0（不生效）。<br/>&lt; 1.0 图像变亮。<br/>&gt; 1.0 图像变暗。</p><p>KCC 9.1.0 及更早版本的默认值为 1.8。</p><p>如需让中间调变暗可使用此选项。</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.gammaBox.setText(QCoreApplication.translate("mainWindow", u"自定义伽马", None))
#if QT_CONFIG(tooltip)
        self.mangaBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p style='white-space:pre'>启用从右到左阅读。</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.mangaBox.setText(QCoreApplication.translate("mainWindow", u"从右到左（漫画）", None))
#if QT_CONFIG(tooltip)
        self.colorBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p style='white-space:pre'>不做灰度转换（保留彩色）。</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.colorBox.setText(QCoreApplication.translate("mainWindow", u"彩色模式", None))
#if QT_CONFIG(tooltip)
        self.titleEdit.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>默认标题</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.titleEdit.setPlaceholderText(QCoreApplication.translate("mainWindow", u"默认标题", None))
#if QT_CONFIG(tooltip)
        self.coverFillBox.setToolTip(QCoreApplication.translate("mainWindow", u"先按宽高比居中裁剪，再把封面缩放到设备精确分辨率。\n根据源图宽高比，可能裁掉上下或左右。Kindle Scribe 不支持此功能。", None))
#endif // QT_CONFIG(tooltip)
        self.coverFillBox.setText(QCoreApplication.translate("mainWindow", u"封面填充", None))
#if QT_CONFIG(tooltip)
        self.smartCoverCropBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>尝试从宽幅图像中裁出主封面。</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.smartCoverCropBox.setText(QCoreApplication.translate("mainWindow", u"智能封面裁剪", None))
#if QT_CONFIG(tooltip)
        self.spreadShiftBox.setToolTip(QCoreApplication.translate("mainWindow", u"横向时把首页偏移到另一侧，以对齐跨页", None))
#endif // QT_CONFIG(tooltip)
        self.spreadShiftBox.setText(QCoreApplication.translate("mainWindow", u"跨页偏移", None))
#if QT_CONFIG(tooltip)
        self.onePageLandscapeBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">未勾选 - 横向双页<br/></span>左右两页各用一个视口</p><p><span style=\" font-weight:600; text-decoration: underline;\">勾选 - 横向单页<br/></span>单页使用一个居中视口</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.onePageLandscapeBox.setText(QCoreApplication.translate("mainWindow", u"单页横向", None))
#if QT_CONFIG(tooltip)
        self.keepComicInfoBox.setToolTip(QCoreApplication.translate("mainWindow", u"保留原有的 ComicInfo.xml 文件。\n\n保留该文件可能导致某些阅读器崩溃，例如 Kobo 自带的 CBZ 阅读器。", None))
#endif // QT_CONFIG(tooltip)
        self.keepComicInfoBox.setText(QCoreApplication.translate("mainWindow", u"保留 ComicInfo.xml", None))
        self.jpegQualityLabel.setText(QCoreApplication.translate("mainWindow", u"JPEG 质量：", None))
#if QT_CONFIG(tooltip)
        self.labelSpreadsButton.setToolTip(QCoreApplication.translate("mainWindow", u"按住 Shift 点击可生成低质量预览。", None))
#endif // QT_CONFIG(tooltip)
        self.labelSpreadsButton.setText(QCoreApplication.translate("mainWindow", u"标注跨页", None))
        self.kofiButton.setText(QCoreApplication.translate("mainWindow", u"在 Ko-fi 上支持我", None))
#if QT_CONFIG(tooltip)
        self.editorButton.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p style='white-space:pre'>按住 Shift 点击可编辑目录。</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.editorButton.setText(QCoreApplication.translate("mainWindow", u"元数据编辑器", None))
        self.humbleButton.setText(QCoreApplication.translate("mainWindow", u"Humble Bundle 推广", None))
#if QT_CONFIG(tooltip)
        self.expertButton.setToolTip(QCoreApplication.translate("mainWindow", u"切换简易/专家模式", None))
#endif // QT_CONFIG(tooltip)
        self.expertButton.setText(QCoreApplication.translate("mainWindow", u"简易/专家模式", None))
#if QT_CONFIG(tooltip)
        self.chunkSizeWidget.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>警告：分块大小高于默认值可能导致<br/>性能与耗电问题，老旧设备尤为明显。</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.chunkSizeLabel.setText(QCoreApplication.translate("mainWindow", u"分块大小 MB：", None))
        self.chunkSizeWarnLabel.setText(QCoreApplication.translate("mainWindow", u"高于默认值可能导致老设备出现性能问题。", None))
        self.easyLabel.setText(QCoreApplication.translate("mainWindow", u"把鼠标悬停在每个选项/按钮上可查看说明！选项支持半选和全选！", None))
    # retranslateUi

