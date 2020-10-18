"""

alias PyQt5, PySide2 -> Qt5

"""

import sys

try:
    import PyQt5
    from PyQt5 import QtCore
    from PyQt5 import QtGui
    from PyQt5 import QtWidgets
    from PyQt5 import QtMultimedia

    sys.modules["Qt5"] = PyQt5
    sys.modules["Qt5.QtCore"] = QtCore
    sys.modules["Qt5.QtGui"] = QtGui
    sys.modules["Qt5.QtWidgets"] = QtWidgets
    sys.modules["Qt5.QtMultimedia"] = QtMultimedia
    # alias
    QtCore.QSlot = QtCore.pyqtSlot
    QtCore.QSignal = QtCore.pyqtSignal
    QtCore.QProperty = QtCore.pyqtProperty
except:
    import PySide2
    from PySide2 import QtCore
    from PySide2 import QtGui
    from PySide2 import QtWidgets
    from PySide2 import QtMultimedia

    sys.modules["Qt5"] = PySide2
    sys.modules["Qt5.QtCore"] = QtCore
    sys.modules["Qt5.QtGui"] = QtGui
    sys.modules["Qt5.QtWidgets"] = QtWidgets
    sys.modules["Qt5.QtMultimedia"] = QtMultimedia
    # alias
    QtCore.QSlot = QtCore.Slot
    QtCore.QSignal = QtCore.Signal
    QtCore.QProperty = QtCore.Property
