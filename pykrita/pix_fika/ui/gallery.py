from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSlot as QSlot
from PyQt5.QtCore import pyqtSignal as QSignal
from PyQt5.QtCore import pyqtProperty as QProperty

from PyQt5.QtWidgets import (
        QWidget,
        QVBoxLayout)


class Gallery(QWidget):
    def __init__(self, parent=None):
        super(Gallery, self).__init__(parent=parent)
        self.setObjectName("pix_fika_gallery_widget")
        self.create_ui()


    def create_ui(self):
        layout = QVBoxLayout()
        self.setLayout(layout)
