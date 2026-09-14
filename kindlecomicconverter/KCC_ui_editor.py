# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MetaEditor.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
from . import KCC_rc

class Ui_editorDialog(object):
    def setupUi(self, editorDialog):
        if not editorDialog.objectName():
            editorDialog.setObjectName(u"editorDialog")
        editorDialog.resize(400, 260)
        editorDialog.setMinimumSize(QSize(400, 260))
        icon = QIcon()
        icon.addFile(u":/Icon/icons/comic2ebook.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        editorDialog.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(editorDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, -1, 5)
        self.editorWidget = QWidget(editorDialog)
        self.editorWidget.setObjectName(u"editorWidget")
        self.gridLayout = QGridLayout(self.editorWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_1 = QLabel(self.editorWidget)
        self.label_1.setObjectName(u"label_1")

        self.gridLayout.addWidget(self.label_1, 0, 0, 1, 1)

        self.seriesLine = QLineEdit(self.editorWidget)
        self.seriesLine.setObjectName(u"seriesLine")

        self.gridLayout.addWidget(self.seriesLine, 0, 1, 1, 1)

        self.label_2 = QLabel(self.editorWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.volumeLine = QLineEdit(self.editorWidget)
        self.volumeLine.setObjectName(u"volumeLine")

        self.gridLayout.addWidget(self.volumeLine, 1, 1, 1, 1)

        self.bulkVolumeCheck = QCheckBox(self.editorWidget)
        self.bulkVolumeCheck.setObjectName(u"bulkVolumeCheck")
        self.bulkVolumeCheck.setVisible(False)

        self.gridLayout.addWidget(self.bulkVolumeCheck, 1, 2, 1, 1)

        self.label_3 = QLabel(self.editorWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.numberLine = QLineEdit(self.editorWidget)
        self.numberLine.setObjectName(u"numberLine")

        self.gridLayout.addWidget(self.numberLine, 3, 1, 1, 1)

        self.label_4 = QLabel(self.editorWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)

        self.writerLine = QLineEdit(self.editorWidget)
        self.writerLine.setObjectName(u"writerLine")

        self.gridLayout.addWidget(self.writerLine, 4, 1, 1, 1)

        self.label_5 = QLabel(self.editorWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)

        self.pencillerLine = QLineEdit(self.editorWidget)
        self.pencillerLine.setObjectName(u"pencillerLine")

        self.gridLayout.addWidget(self.pencillerLine, 5, 1, 1, 1)

        self.label_6 = QLabel(self.editorWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 1)

        self.inkerLine = QLineEdit(self.editorWidget)
        self.inkerLine.setObjectName(u"inkerLine")

        self.gridLayout.addWidget(self.inkerLine, 6, 1, 1, 1)

        self.label_7 = QLabel(self.editorWidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 7, 0, 1, 1)

        self.coloristLine = QLineEdit(self.editorWidget)
        self.coloristLine.setObjectName(u"coloristLine")

        self.gridLayout.addWidget(self.coloristLine, 7, 1, 1, 1)

        self.label_8 = QLabel(self.editorWidget)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 2, 0, 1, 1)

        self.titleLine = QLineEdit(self.editorWidget)
        self.titleLine.setObjectName(u"titleLine")

        self.gridLayout.addWidget(self.titleLine, 2, 1, 1, 1)


        self.verticalLayout.addWidget(self.editorWidget)

        self.optionWidget = QWidget(editorDialog)
        self.optionWidget.setObjectName(u"optionWidget")
        self.horizontalLayout = QHBoxLayout(self.optionWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.statusLabel = QLabel(self.optionWidget)
        self.statusLabel.setObjectName(u"statusLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusLabel.sizePolicy().hasHeightForWidth())
        self.statusLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.statusLabel)

        self.okButton = QPushButton(self.optionWidget)
        self.okButton.setObjectName(u"okButton")
        self.okButton.setMinimumSize(QSize(0, 30))
        icon1 = QIcon()
        icon1.addFile(u":/Other/icons/convert.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.okButton.setIcon(icon1)

        self.horizontalLayout.addWidget(self.okButton)

        self.cancelButton = QPushButton(self.optionWidget)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setMinimumSize(QSize(0, 30))
        icon2 = QIcon()
        icon2.addFile(u":/Other/icons/clear.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.cancelButton.setIcon(icon2)

        self.horizontalLayout.addWidget(self.cancelButton)


        self.verticalLayout.addWidget(self.optionWidget)

        QWidget.setTabOrder(self.seriesLine, self.volumeLine)
        QWidget.setTabOrder(self.volumeLine, self.bulkVolumeCheck)
        QWidget.setTabOrder(self.bulkVolumeCheck, self.titleLine)
        QWidget.setTabOrder(self.titleLine, self.numberLine)
        QWidget.setTabOrder(self.numberLine, self.writerLine)
        QWidget.setTabOrder(self.writerLine, self.pencillerLine)
        QWidget.setTabOrder(self.pencillerLine, self.inkerLine)
        QWidget.setTabOrder(self.inkerLine, self.coloristLine)
        QWidget.setTabOrder(self.coloristLine, self.okButton)
        QWidget.setTabOrder(self.okButton, self.cancelButton)

        self.retranslateUi(editorDialog)

        QMetaObject.connectSlotsByName(editorDialog)
    # setupUi

    def retranslateUi(self, editorDialog):
        editorDialog.setWindowTitle(QCoreApplication.translate("editorDialog", u"元数据编辑器", None))
        self.label_1.setText(QCoreApplication.translate("editorDialog", u"系列：", None))
        self.label_2.setText(QCoreApplication.translate("editorDialog", u"卷号：", None))
#if QT_CONFIG(tooltip)
        self.bulkVolumeCheck.setToolTip(QCoreApplication.translate("editorDialog", u"<b>批量卷号编辑</b><br>勾选后可为多个文件批量指定卷号。<br><br><b>输入格式：</b><br><code>5</code> → 从 5 开始的序列（5, 6, 7……）<br><code>1-10</code> → 1 到 10 的范围<br><code>1, 3, 5</code> → 指定具体数值<br><br><i>注意：分配前会先按字母顺序对文件排序。</i>", None))
#endif // QT_CONFIG(tooltip)
        self.bulkVolumeCheck.setText("")
        self.label_3.setText(QCoreApplication.translate("editorDialog", u"期号：", None))
        self.label_4.setText(QCoreApplication.translate("editorDialog", u"编剧：", None))
        self.label_5.setText(QCoreApplication.translate("editorDialog", u"作画：", None))
        self.label_6.setText(QCoreApplication.translate("editorDialog", u"墨线：", None))
        self.label_7.setText(QCoreApplication.translate("editorDialog", u"上色：", None))
        self.label_8.setText(QCoreApplication.translate("editorDialog", u"标题：", None))
        self.statusLabel.setText("")
        self.okButton.setText(QCoreApplication.translate("editorDialog", u"保存", None))
        self.cancelButton.setText(QCoreApplication.translate("editorDialog", u"取消", None))
    # retranslateUi

