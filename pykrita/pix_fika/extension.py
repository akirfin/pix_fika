"""

PixFika for Krita

"""

import re
from urllib import request
from urllib.parse import urlparse

from krita import (
        Krita,
        Extension)

from .common.utils_py import (
        first,
        last,
        underscore)

from .common.utils_qt import (
        find_menu,
        create_menu,
        create_action)

from .common.utils_kis import (
        find_create_experimental_menu,
        write_extension_action_file,
        read_setting,
        write_setting)

from .ui.main_window import (
        MainWindow, )


class PixFikaExtension(Extension):
    def __init__(self, parent):
        super(PixFikaExtension, self).__init__(parent)
        self.setObjectName("pix_fika_extension")
        self._window = None


    def setup(self):
        """
        Called once in Krita startup.
        """
        app = Krita.instance()
        extension_name = self.objectName()
        # hook app closing
        notifier = app.notifier()
        notifier.applicationClosing.connect(self.shuttingDown)
        # read defaults from settings
        #self._shader_toy_user = read_setting(
        #        extension_name,
        #        self.shader_toy_user_attr,
        #        default="https://krita-artists.org/tag/featured")
        # create actions here and share "instance" to other places.
        self._show_window_action = create_action(
                name="pix_fika_show_window",
                text=i18n("Show PixFika Window"),
                triggered=self.show_window,
                parent=self)  # I own the action!
        # when is .action file applied?
        # write_extension_action_file(self)


    def shuttingDown(self):
        """
        Called once in Krita shutting down.
        """
        extension_name = self.objectName()
        #write_setting(
        #        extension_name,
        #        self.shader_toy_user_attr,
        #        self._shader_toy_user)


    def createActions(self, window):
        """
        Called once for each new window opened in Krita.
        """
        menu = find_create_experimental_menu(window)
        menu.addAction(self._show_window_action)


    def show_window(self, cheched=None):
        if self._window is None:
            self._window = MainWindow()
        self._window.show()
