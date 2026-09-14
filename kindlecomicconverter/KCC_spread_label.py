import os

from PySide6.QtCore import (Qt)
from PySide6.QtGui import (QKeyEvent, QPixmap)
from PySide6.QtWidgets import (QHBoxLayout, QLabel, QDialog)

class LabelSpreadsDialog(QDialog):
    def __init__(self, available_height, images, spreads):
        super().__init__()
        self.index = 0
        self.images = images 
        self.spreads = spreads
        self.index2page = {i: os.path.basename(image) for i, image in enumerate(images)}

        self.setWindowTitle("TODO: Filename goes here")
        # self.setGeometry(APP.primaryScreen().availableGeometry())
        # self.setMaximumSize(APP.primaryScreen().availableSize())
        self.available_height = available_height

        layout = QHBoxLayout()
        self.setLayout(layout)
        
        label = QLabel()
        label2 = QLabel()
        self.label = label
        self.label2 = label2
        layout.addWidget(label)
        layout.addWidget(label2)
        # 用独立布尔状态记录当前页是否已标记为跨页，不依赖标签文字判断
        self.isSpread = self.index2page[self.index] in self.spreads
        label2.setText('跨页' if self.isSpread else '不是跨页')

        help_text = [
            "使用方向键切换页面。",
            "按空格键确认跨页。",
            "使用跨页偏移选项可整体偏移 1 页。",
            "按回车键确认所有跨页标记。",
            "关闭窗口可取消。"
        ]
        buttonLabel = QLabel('\n'.join(help_text))
        layout.addWidget(buttonLabel)
        # print(label.size())
        # print(label.maximumSize())
        # l, t, r, b = layout.getContentsMargins()
        
        #label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        pixmap = QPixmap(images[0]).scaledToHeight(self.available_height * 0.9)
        label.setPixmap(pixmap)
        #label.setScaledContents(True)
        
        #label2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # pixmap2 = QPixmap(images[0]).scaledToHeight(self.frameGeometry().height() - t - b - t - b)
        # label2.setPixmap(pixmap2)
        #label2.setScaledContents(True)
        #self.resize(pixmap2.width(), pixmap2.height())

    def _refreshSpreadState(self):
        self.isSpread = self.index2page[self.index] in self.spreads
        self.label2.setText('跨页' if self.isSpread else '不是跨页')

    def keyReleaseEvent(self, event):
        # t = 20
        # b = 20
        if isinstance(event, QKeyEvent):
            if event.key() == Qt.Key.Key_Left:
                self.index = max(0, self.index - 1)
                self._refreshSpreadState()
                pixmap = QPixmap(self.images[self.index]).scaledToHeight(self.available_height * 0.9)
                self.label.setPixmap(pixmap)
                # pixmap2 = QPixmap(images[self.index]).scaledToHeight(self.frameGeometry().height() - t - b - t - b)
                # self.label2.setPixmap(pixmap2)
            elif event.key() == Qt.Key.Key_Right:
                self.index = min(self.index + 1, len(self.images) - 1)
                self._refreshSpreadState()
                
                pixmap = QPixmap(self.images[self.index]).scaledToHeight(self.available_height * 0.9)
                self.label.setPixmap(pixmap)
                # pixmap2 = QPixmap(images[self.index]).scaledToHeight(self.frameGeometry().height() - t - b - t - b)
                # self.label2.setPixmap(pixmap2)
            elif event.key() == Qt.Key.Key_Space:
                if self.isSpread:
                    self.spreads.remove(os.path.basename(self.images[self.index]))
                else:
                    self.spreads.append(os.path.basename(self.images[self.index]))
                self._refreshSpreadState()
            elif event.key() == Qt.Key.Key_Return or event.key() == Qt.Key.Key_Enter:
                self.accept()
            else:
                super().keyReleaseEvent(event)
        else:
            super().keyReleaseEvent(event)