import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk,GdkPixbuf

def btn_clicked(widget):
    print(widget.get_label())

pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(filename="icon.png", width=24, height=24, preserve_aspect_ratio=True)
img = Gtk.Image.new_from_pixbuf(pixbuf)
btn = Gtk.Button(label='some text',image=img,)
btn.connect('clicked',btn_clicked)
win = Gtk.Window()
win.connect("destroy", Gtk.main_quit)
win.add(btn)
win.show_all()
Gtk.main()
