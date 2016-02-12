from gi.repository import Gtk

class QueryWindow(Gtk.Box):
    """
        Query builder interface
    """
    def __init__(self):
        super(QueryWindow, self).__init__(orientation=Gtk.Orientation.VERTICAL)

        self._init_textview()
        self._init_wrapbox()

        self.textview.set_editable(True)
        self.textview.set_cursor_visible(True)

    def _init_textview(self):
        """ TODO Move to glade
        """
        scrolledwindow = Gtk.ScrolledWindow()
        scrolledwindow.set_hexpand(True)
        scrolledwindow.set_vexpand(True)
        self.add(scrolledwindow)

        self.textview = Gtk.TextView()
        self.textbuffer = self.textview.get_buffer()
        scrolledwindow.add(self.textview)

    def _init_wrapbox(self):
        """ TODO Move to glade
        """
        wrap_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(wrap_box)

        radio_wrapnone = Gtk.RadioButton.new_with_label_from_widget(None, "No Wrapping")
        radio_wrapnone.connect("toggled", self.on_wrap_toggled, Gtk.WrapMode.NONE)
        wrap_box.add(radio_wrapnone)

        radio_wrapchar = Gtk.RadioButton.new_with_label_from_widget(radio_wrapnone, "Character Wrapping")
        radio_wrapchar.connect("toggled", self.on_wrap_toggled, Gtk.WrapMode.CHAR)
        wrap_box.add(radio_wrapchar)

        radio_wrapword = Gtk.RadioButton.new_with_label_from_widget(radio_wrapnone, "Word Wrapping")
        radio_wrapword.connect("toggled", self.on_wrap_toggled, Gtk.WrapMode.WORD)
        wrap_box.add(radio_wrapword)

    def on_wrap_toggled(self, widget, mode):
        """ TODO Move to glade
        """
        self.textview.set_wrap_mode(mode)
