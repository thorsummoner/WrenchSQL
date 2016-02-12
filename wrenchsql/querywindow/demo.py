import signal
from gi.repository import Gtk

import wrenchsql.querywindow

def demo():
    window = Gtk.Window(title='demo querywindow')
    window.connect('delete-event', Gtk.main_quit)
    querywindow = wrenchsql.querywindow.QueryWindow()
    window.add(querywindow)
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    window.show_all()
    Gtk.main()
