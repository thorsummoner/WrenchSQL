import signal
from gi.repository import Gtk
from wrenchsql.querywindow.gtk import QueryWindow

def main():
    window = Gtk.Window(title='demo querywindow')
    window.connect('delete-event', Gtk.main_quit)

    signal.signal(signal.SIGINT, signal.SIG_DFL)
    querywindow = QueryWindow()
    window.add(querywindow)
    window.show_all()
    Gtk.main()
