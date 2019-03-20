#!/usr/bin/env python
# Our main.py with all the functionality included.
import gi
from gi.repository import Gtk
gi.require_version('Gtk', '3.0')



def hello(button):
    print('Hello something...')

handlers = {
        'onDestroy' : Gtk.main_quit,
        'onButtonPressed' : hello
}

builder = Gtk.Builder()
builder.add_from_file('Sample0.glade')
builder.connect_signals(handlers)

window = builder.get_object('window1')
window.show_all()

Gtk.main()
