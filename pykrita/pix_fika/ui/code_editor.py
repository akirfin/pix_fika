from PyQt5.QtCore import (
        Qt,
        pyqtSlot as QSlot,
        pyqtSignal as QSignal,
        pyqtProperty as QProperty)

from PyQt5.QtWidgets import (
        QWidget,
        QVBoxLayout)


class CodeEditor(QWidget):
    def __init__(self, parent=None):
        super(CodeEditor, self).__init__(parent=parent)
        self.setObjectName("pix_fika_code_editor")
        self.create_ui()


    def create_ui(self):
        layout = QVBoxLayout()
        self.setLayout(layout)
