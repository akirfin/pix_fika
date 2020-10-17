"""

Register & Unregister plugin for Krita.

ToDo:
    - can loaded modules be tracked before / after load?

"""

__version__ = "0.0.1"

import sys
import os

try:
    from krita import (
            Krita,
            DockWidgetFactory,
            DockWidgetFactoryBase)


    def register():
        """
        Register Krita plugin.
        Add extensions & dockers to Krita.
        """
        from .extension import (
                PixFikaExtension, )

        app = Krita.instance()
        extensions = (type(e) for e in app.extensions())
        if PixFikaExtension not in extensions:
            extension = PixFikaExtension(app)
            app.addExtension(extension)


    def unregister():
        """
        Not supported by Krita :.(

        Remove extensions & dockers from Krita.
        Unload plugin modules from python ???
        """
        from .extension import (
                PixFikaExtension, )

        app = Krita.instance()
        extensions = {type(e): e for e in app.extensions()}
        extension = extensions.get(PixFikaExtension)
        if extension:
            app.removeExtension(extension)

        del sys.modules["Extension modules..."]


    register()
except:
    pass
