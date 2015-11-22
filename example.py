#!/usr/bin/env python

import gladewindow
import os

class ExampleWindow(gladewindow.BaseWindow):
    """
        Gui application interface.
    """

    GLADE_FILE = os.path.join(os.path.dirname(__file__), '.glade')

    def __init__(self):
        super(ExampleWindow, self).__init__()


    class Handler(gladewindow.BaseHandler):
        """
            Main Window Event Handler
        """


if __name__ == '__main__':
    exit(ExampleWindow().main())
