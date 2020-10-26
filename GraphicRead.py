import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GLib
import threading
from Read import Rfid


class MyWindow(Gtk.Window):
    def __init__(self):

        # creating window
        Gtk.Window.__init__(self, title="Scan RFID")
        self.set_border_width(10)
        self.connect("destroy", Gtk.main_quit)

        # creating Box and adding it to window
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=15)
        self.add(self.box)

        # creating EventBox
        self.evbox = Gtk.EventBox()
        self.evbox.override_background_color(0, Gdk.RGBA(0.2,0.2,0.8,0.4))

        # creating Label and adding it to the box
        self.lbl = Gtk.Label("Please, login with your university card")
        self.lbl.set_size_request(500, 100)
        self.lbl.set_use_markup(True)
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
        GLib.idle_add(self.lbl.set_text,"UID:"+uid)
        self.evbox.override_background_color(0, Gdk.RGBA(0.8,0,0.2,0.6))

        #creating function that executes when the button is pressed
    def btn_pressed(self, widget):
        self.lbl.set_label("Please, login with your university card")         
        self.evbox.override_background_color(0, Gdk.RGBA(0.2,0.2,0.8,0.4))
        thread = threading.Thread(target=self.uid_read)
        thread.start()

win = MyWindow()