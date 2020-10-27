import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GLib
import threading
from Read import Rfid


class MyWindow(Gtk.Window):
    def __init__(self):

        # creating css
        #css = b'* { background-color: #8bb; }'
        #css_provider = Gtk.CssProvider()
        #css_provider.load_from_data(css)
        #context = Gtk.StyleContext()
        #screen = Gdk.Screen.get_default()
        #context.add_provider_for_screen(screen, css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

        # creating window
        Gtk.Window.__init__(self, title="Scan RFID")
        self.set_border_width(10)
        self.connect("destroy", Gtk.main_quit)

        # creating Box and adding it to window
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=15)
        self.add(self.box)

        # creating EventBox
        self.evbox = Gtk.EventBox()
        self.evbox.override_background_color(0, Gdk.RGBA(0.2,0.2,0.8,1))

        # creating Label and adding it to the box
        self.lbl = Gtk.Label('<span foreground="white" size="x-large">Please, login with your university card</span>')
        self.lbl.set_size_request(500, 100)
        self.lbl.set_use_markup(True)
        self.lbl.set_name("login_label")
        self.evbox.add(self.lbl)

        # creating Button and adding it to the box
        self.btn = Gtk.Button(label="Clear")
        self.btn.connect("clicked", self.btn_pressed)
        self.box.pack_start(self.evbox, True, True, 0)
        self.box.pack_start(self.btn, True, True, 0)

        # creating and starting a Thread
        thread = threading.Thread(target=self.uid_read)
        thread.daemon = True
        thread.start()

        # showing everything
        self.show_all()
        Gtk.main()

        #creating function that reads and displays uid(connected to Thread) 
    def uid_read(self):
        rf = Rfid()
        uid = rf.read_uid()
        GLib.idle_add(self.lbl.set_label,'<span foreground="white" size="x-large">uid: '+uid+'</span>')
        #css = b'#login_label {background-color: #f00;}'
        GLib.idle_add(self.evbox.override_background_color,0, Gdk.RGBA(0.8,0,0.2,1))

        #creating function that executes when the button is pressed
    def btn_pressed(self, widget):
        self.lbl.set_label('<span foreground="white" size="x-large">Please, login with your university card</span>')
        #css = b'#login_label {background-color: #8bb;}'         
        self.evbox.override_background_color(0, Gdk.RGBA(0.2,0.2,0.8,1))
        thread = threading.Thread(target=self.uid_read)
        thread.start()

win = MyWindow()