from gi.repository import Gtk
from gi.repository import GtkSource
from gi.repository import Gdk
from gi.repository import GObject

GTK_ICON_SIZE_MENU = Gtk.icon_size_from_name('gtk-menu')
UNTITLED = 'untitled'
SPACING = 5

class QueryWindow(Gtk.Overlay):
    """
        Query builder interface
    """
    def __init__(self):
        super(QueryWindow, self).__init__()

        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(self.box)

        self._init_notebook()
        self._init_wrapbox()

        self.textview.set_editable(True)
        self.textview.set_cursor_visible(True)

    def _notebook_on_button(self, widget, event):
        if event.type is Gdk.EventType._2BUTTON_PRESS:
            print(event.type)

        self._last_notebook_event = event

    def _init_notebook(self):
        self.notebook = Gtk.Notebook()
        self.notebook.connect('button-press-event', self._notebook_on_button)
        self.box.add(self.notebook)

        self._init_textview()

    def _init_textview(self):
        """ TODO Move to Class
        """
        label = Gtk.Label(UNTITLED)
        fancy_label = Gtk.Box(spacing=SPACING)
        fancy_label.add(Gtk.Image.new_from_icon_name('text-x-generic', GTK_ICON_SIZE_MENU))
        fancy_label.add(label)
        fancy_label.add(Gtk.Button.new_from_icon_name('gtk-close', GTK_ICON_SIZE_MENU))
        fancy_label.show_all()

        scrolledwindow = Gtk.ScrolledWindow()
        scrolledwindow.set_hexpand(True)
        scrolledwindow.set_vexpand(True)
        scrolledwindow.set_shadow_type(Gtk.ShadowType.IN)

        self.textview = GtkSource.View()
        if 'sourceview_options':
            self.textview.set_show_line_numbers(True)
            self.textview.set_show_line_marks(True)
            self.textview.set_tab_width(4)
            self.textview.set_auto_indent(True)
            self.textview.set_insert_spaces_instead_of_tabs(True)
            self.textview.set_show_right_margin(True)
            self.textview.set_highlight_current_line(True)

            # # someday
            # self.textview.set_monospace(True)
            from gi.repository import Pango
            self.textview.override_font(
                Pango.font_description_from_string('Monospace 10')
            )


        if 'source_language':
            language_manager = GtkSource.LanguageManager()
            lang_sql = language_manager.get_language('sql')

            self.textbuffer = GtkSource.Buffer.new_with_language(lang_sql)

        self.textview.set_buffer(self.textbuffer)

        scrolledwindow.add(self.textview)

        self.notebook.append_page_menu(
            child=scrolledwindow,
            tab_label=fancy_label,
            menu_label=label,
        )

    def _init_wrapbox(self):
        """ TODO Move to glade
        """
        wrap_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.box.add(wrap_box)

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
