import platform
import ctypes

from gi.repository import Gtk

import wrenchsql.querywindow.gtk.platform

class QueryWindow(Gtk.Bin):
    def __init__(self):
        super(QueryWindow, self).__init__()

        self.platform_info = getattr(
            # Supported Platforms
            wrenchsql.querywindow.gtk.platform,
            # Current Distribution
            platform.linux_distribution()[0]
        )

        self.libgtksourceview3 = ctypes.cdll.LoadLibrary(
            self.platform_info.libgtksourceview3
        )

        gtk_sourceview = self.libgtksourceview3.gtk_source_view_new()
