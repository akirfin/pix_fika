"""
Common small scripts for Qt
"""
import re
from urllib import request
from contextlib import contextmanager

from Qt5.QtCore import (
        Qt, )

from Qt5.QtGui import (
        QPainter,
        QPalette,
        QColor,
        QImage)

from Qt5.QtWidgets import (
        QAction,
        QMenu)

from .utils_py import (
        print_console,
        first,
        last)


def get_enum_str(owner_cls, enum_cls, enum_value):
    """
    Translate Qt enum to enum name string.
    "I am not a number! I'm a free man!"
    """
    for attr_name in dir(owner_cls):
        attr = getattr(owner_cls, attr_name)
        if isinstance(attr, enum_cls) and (attr == enum_value):
            return attr_name


def dump_qobject_tree(qobj):
    """
    Dump QObject hierarchy.
    """
    for q, depth in walk_qobjects([qobj]):
        indent = "    " * depth
        name = q.objectName()
        cls = type(q).__name__
        meta_cls = q.metaObject().className()
        text = ""
        try:
            text = q.text()
        except:
            pass
        print_console("{indent}objectName: \"{name}\", text: \"{text}\", cls: {cls}, meta_cls: {meta_cls}".format(**locals()))


def walk_qobjects(qobjs, depth_first=True):
    """
    Traverse QObject tree.
    """
    stack = list((q, 0) for q in qobjs)
    while stack:
        qobj, depth = stack.pop(0 if depth_first else -1)
        yield qobj, depth
        stack[0:0] = ((q, depth +1) for q in qobj.children())


def walk_qobject_ancestors(qobj):
    """
    Traverse QObject ancestors.
    """
    cursor = qobj.parent()
    while cursor:
        yield cursor
        cursor = cursor.parent()


@contextmanager
def create_painter(obj):
    """
    Create QPainter context.
    (newer again app hangs, because exeption while painting!)
    """
    painter = QPainter(obj)
    try:
        yield painter
    finally:
        painter.end()


@contextmanager
def keep_painter(painter):
    """
    Push & Pop painter context.
    """
    painter.save()
    try:
        yield painter
    finally:
        painter.restore()


@contextmanager
def block_signals(*objs, state=True):
    """
    Disable / Enable signal sending state of QObjects,
    for duration of context.
    """
    old_states = list()
    for obj in objs:
        old_state = obj.blockSignals(state)
        old_states.append((obj, old_state))
    try:
        yield state
    finally:
        for obj, old_state in old_states:
            obj.blockSignals(old_state)


def dump_menu(menu):
    """
    Dump QMenu item hierarchy.
    menubar = Krita.instance().activeWindow().qwindow().menuBar()
    """
    for act, depth in walk_menu(menu):
        indent = depth * "    "
        name = act.objectName()
        text = act.text() or ""
        cls = type(act)
        print('{indent}("{name}", "{text}")'.format(**locals()))


def walk_menu(qmenu):
    """
    Menu contains actions,
        and some actions have a menu,
            and it contains actions ...
    """
    stack = list((a, 0) for a in qmenu.actions())
    while stack:
        act, depth = stack.pop(0)
        yield act, depth
        sub_menu = act.menu()
        if sub_menu:
            stack[0:0] = ((a, depth +1) for a in sub_menu.actions())


def find_menu(root_menu, menu_path):
    menu = root_menu
    for entry in menu_path.strip("/").split("/"):
        menu = first((a.menu() for a in menu.actions() if a.objectName() == entry), None)
        if menu is None:
            break  # no point to continue!
    return menu


def create_menu(
            name,
            title,
            parent=None):
    menu = QMenu(title, parent=parent)
    menu.setObjectName(name)
    menu.menuAction().setObjectName(name)
    return menu


def create_action(
            name=None,
            text=None,
            icon=None,
            icon_text=None,
            icon_in_menu=None,
            shortcut=None,
            tip=None,
            status_tip=None,
            what=None,
            visible=None,
            enabled=None,
            checkable=None,
            checked=None,
            font=None,
            data=None,
            triggered=None,
            parent=None):
    """
    Action hero!
    """
    action = QAction(parent)
    if name is not None:
        action.setObjectName(name)
    if text is not None:
        action.setText(text)
    if icon is not None:
        action.setIcon (icon)
    if icon_text is not None:
        action.setIconText(icon_text)
    if icon_in_menu is not None:
        action.setIconVisibleInMenu(icon_in_menu)
    if shortcut is not None:
        action.setShortcut(shortcut)
    if tip is not None:
        action.setToolTip(tip)
    if status_tip is not None:
        action.setStatusTip(status_tip)
    if what is not None:
        action.setWhatsThis(what)
    if visible is not None:
        action.setVisible(visible)
    if enabled is not None:
        action.setEnabled(enabled)
    if checkable is not None:
        action.setCheckable(checkable)
    if checked is not None:
        action.setChecked(checked)
    if font is not None:
        action.setFont(font)
    if data is not None:
        action.setData(data)
    if triggered is not None:
        action.triggered.connect(triggered)
    return action


def dark_palette():
    """
    Let there be darkness!
    """
    dark_palette = QPalette()
    dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.WindowText, QColor(220, 220, 220))
    dark_palette.setColor(QPalette.Disabled, QPalette.WindowText, QColor(127, 127, 127))
    dark_palette.setColor(QPalette.Base, QColor(40, 40, 40))
    dark_palette.setColor(QPalette.AlternateBase, QColor(255, 255, 255, 15))  # damit!
    dark_palette.setColor(QPalette.ToolTipBase, QColor(60, 60, 60))
    dark_palette.setColor(QPalette.ToolTipText, QColor(220, 220, 200))
    dark_palette.setColor(QPalette.Text, QColor(220, 220, 220))
    dark_palette.setColor(QPalette.Disabled, QPalette.Text, QColor(60, 60, 60))

    dark_palette.setColor(QPalette.Light, QColor(220, 220, 220))
    dark_palette.setColor(QPalette.Midlight, QColor(150, 150, 150))
    dark_palette.setColor(QPalette.Button, QColor(90, 90, 90))
    dark_palette.setColor(QPalette.Mid, QColor(64, 64, 64))
    dark_palette.setColor(QPalette.Dark, QColor(35, 35, 35))
    dark_palette.setColor(QPalette.Shadow, QColor(10, 10, 10))

    dark_palette.setColor(QPalette.ButtonText, QColor(255, 255, 255))
    dark_palette.setColor(QPalette.Disabled, QPalette.ButtonText, QColor(127, 127, 127))
    dark_palette.setColor(QPalette.BrightText, QColor(220, 220, 10))
    dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.Highlight, QColor(255, 127, 0))
    dark_palette.setColor(QPalette.Disabled, QPalette.Highlight, QColor(80, 80, 80))  # oxymoran?
    dark_palette.setColor(QPalette.HighlightedText, Qt.white)
    dark_palette.setColor(QPalette.Disabled, QPalette.HighlightedText, QColor(127, 127, 127))
    return dark_palette


def fetch_qimage_from_url(image_url):
    """
    Download image from url. (blocking!)
    Uses python standard library.
    """
    name = image_url.rsplit("/", 1)[-1]  # strip path
    name = name.split(".", 1)[0]  # strip ext
    r = request.urlopen(image_url)
    if r.getcode() == 200:
        image = QImage()
        image.loadFromData(r.read())
        return image
