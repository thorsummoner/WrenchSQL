import signal
from gi.repository import Gtk

def main():
    window = Gtk.Window(title='demo querywindow')
    window.connect('delete-event', Gtk.main_quit)

    signal.signal(signal.SIGINT, signal.SIG_DFL)
    window.show_all()
    Gtk.main()
