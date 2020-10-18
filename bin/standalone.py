#!/usr/bin/env python3

"""

Run Standalone Pix Fika

"""

import sys
import os

here_dir = os.path.dirname(__file__)
pykrita_dir = os.path.abspath(os.path.join(here_dir, "..", "pykrita"))
sys.path.append(pykrita_dir)

import pix_fika.common.Qt5

from Qt5.QtWidgets import QApplication

from pix_fika.common.utils_qt import (
        dark_palette, )

from pix_fika.ui.main_window import (
        MainWindow, )


if __name__ == "__main__":
    app = QApplication()
    app.setStyle("Fusion")
    app.setPalette(dark_palette())

    win = MainWindow()
    win.show()

    sys.exit(app.exec_())
