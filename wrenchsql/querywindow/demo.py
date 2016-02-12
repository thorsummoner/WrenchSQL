import signal
from gi.repository import Gtk

import wrenchsql.querywindow

def demo():
    window = Gtk.Window(title='demo querywindow')
    window.connect('delete-event', Gtk.main_quit)
    container = Gtk.Box()
    container.set_border_width(10)
    window.add(container)

    querywindow = wrenchsql.querywindow.QueryWindow()
    container.add(querywindow)
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    window.show_all()
    Gtk.main()
