"""
import this and then Qt5 points to PyQt5 or PySide2.
"""

import sys

try:
    import PyQt5
    from PyQt5 import QtCore
    from PyQt5 import QtGui
    from PyQt5 import QtWidgets

    sys.modules["Qt5"] = PyQt5
    sys.modules["Qt5.QtCore"] = QtCore
    sys.modules["Qt5.QtGui"] = QtGui
    sys.modules["Qt5.QtWidgets"] = QtWidgets
    # alias
    QtCore.QSlot = QtCore.pyqtSlot
    QtCore.QSignal = QtCore.pyqtSignal
    QtCore.QProperty = QtCore.pyqtProperty
except:
    import PySide2
    from PySide2 import QtCore
    from PySide2 import QtGui
    from PySide2 import QtWidgets

    sys.modules["Qt5"] = PySide2
    sys.modules["Qt5.QtCore"] = QtCore
    sys.modules["Qt5.QtGui"] = QtGui
    sys.modules["Qt5.QtWidgets"] = QtWidgets
    # alias
    QtCore.QSlot = QtCore.Slot
    QtCore.QSignal = QtCore.Signal
    QtCore.QProperty = QtCore.Property
