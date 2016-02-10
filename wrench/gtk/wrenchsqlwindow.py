
import os
import wrench.gtk.gladewindow as gladewindow


#PRUNE
import os
import logging
from gi.repository import GObject, Gtk, Gio, GdkPixbuf
from wrench.shell import Shell

logging.basicConfig()
LOG_LEVEL = logging.DEBUG
logger = logging.getLogger(__name__)
logger.setLevel(LOG_LEVEL)

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
STOCK_DBSHELL = "dbshell"
STOCK_SERVER = "server"
STOCK_PYTHON = "python"
#ENDPRUNE

class WrenchSqlWindow(gladewindow.BaseWindow):
    """
        Gui application interface.
    """

    GLADE_FILE = os.path.join(os.path.dirname(__file__), '.glade')

    def __init__(self):
        super(WrenchSqlWindow, self).__init__()
        self._add_shell_panel()


    def _add_shell_panel(self):
        """ Adds a python shell to the bottom pane. """
        logger.debug("Adding shell.")
        self._shell = Shell()
        self._shell.set_font("monospace 10")
        self.add(self._shell)


    class Handler(gladewindow.BaseHandler):
        """
            Main Window Event Handler
        """
