from Qt5.QtCore import (
        Qt,
        QSlot,
        QSignal,
        QProperty)

from Qt5.QtWidgets import (
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
