import os

try:
    from PyQt5.QtCore import (
            Qt,
            pyqtSlot as QSlot,
            pyqtSignal as QSignal,
            pyqtProperty as QProperty)

    from PyQt5.QtWidgets import (
            QMainWindow,
            QWidget,
            QStackedLayout)
except:
    from PySide2.QtCore import (
            Qt,
            Slot as QSlot,
            Signal as QSignal,
            Property as QProperty)

    from PySide2.QtWidgets import (
            QMainWindow,
            QWidget,
            QStackedLayout)

from .gallery import (
        Gallery, )

from .graph_view import (
        GraphView, )

from .code_editor import (
        CodeEditor, )


class MainWindow(QMainWindow):
    """
    Window for Pix Fika.
        - graph editor (nodes & edges)
            - shader program
            - shader
                - type (FRAGMENT, GEOMETRY, VERTEX, ...)
                - uniforms (widget type)
                - uniform default values ($TIME_UTC_MS, $MOUSE, $PEN, ...))
                - code
            - texture node
                - type
                - wrap
                - filering
                - media source ($SOUND_CLOUD, $KEYBOARD, ...)
    """
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setObjectName("pix_fika_main_window")
        self.setWindowTitle("𝓟𝓲𝔁𝓕𝓲𝓴𝓪 0.0.1")
        self.create_ui()


    def create_ui(self):
        self.resize(960, 600)
        central = GraphView()
        self.setCentralWidget(central)

        layout = QStackedLayout()
        central.setLayout(layout)

        self._shader_editor = CodeEditor()
        layout.addWidget(self._shader_editor)

        self._gallery = Gallery()
        layout.addWidget(self._gallery)
