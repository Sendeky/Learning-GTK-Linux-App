import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class MainWindow(Gtk.Window):
    
    def __init__(self):
        super().__init__(title="MainWindow")
        # border around topmost level object in main window
        self.set_border_width(10)

        # box with buttons
        self.box = Gtk.Box(spacing=6)
        self.add(self.box) 

        # button1 
        self.button1 = Gtk.Button(label="Hello")
        self.button1.connect("clicked", self.on_button1_clicked)
        # guessing "pack_start" is similar to leading_margin in iOS?
        self.box.pack_start(self.button1, True, True, 0)

        # button2
        self.button2 = Gtk.Button(label="Goodbye")
        self.button2.connect("clicked", self.on_button2_clicked)
        self.box.pack_start(self.button2, True, True, 0)

        # button3
        self.button3 = Gtk.Button(label="Maybe")
        self.button3.connect("clicked", self.on_button3_clicked)
        self.box.pack_start(self.button3, True, True, 0)

        # label
        self.label1 = Gtk.Label(label="Label1")
        self.box.pack_start(self.label1, True, False, 0)

    def on_button1_clicked(self, widget):
        print("Hello!")

    def on_button2_clicked(self, widget):
        print("Goodbye!")

    def on_button3_clicked(self, widget):
        print("Maybe!")

win = MainWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
