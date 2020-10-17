import os

from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSlot as QSlot
from PyQt5.QtCore import pyqtSignal as QSignal
from PyQt5.QtCore import pyqtProperty as QProperty

from PyQt5.QtWidgets import (
        QMainWindow,
        QWidget,
        QStackedLayout)

from .gallery import (
        Gallery, )

from .graph_view import (
        GraphView, )


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
        self.create_ui()


    def create_ui(self):
        central = GraphView()
        self.setCentralWidget(central)

        layout = QStackedLayout()
        central.setLayout(layout)

        self._shader_editor = EditorWidget()
        layout.addWidget(self._shader_editor)

        self._gallery = GalleryWidget()
        layout.addWidget(self._gallery)
