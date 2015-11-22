
import os
import wrench.gladewindow as gladewindow

class WrenchSqlWindow(gladewindow.BaseWindow):
    """
        Gui application interface.
    """

    GLADE_FILE = os.path.join(os.path.dirname(__file__), '.glade')

    def __init__(self):
        super(WrenchSqlWindow, self).__init__()


    class Handler(gladewindow.BaseHandler):
        """
            Main Window Event Handler
        """
