# https://github.com/Andereoo/TkinterWeb
# no javascript for this package
from tkinterweb import HtmlFrame #import the HTML browser
try:
  import tkinter as tk #python3
except ImportError:
  import Tkinter as tk #python2

root = tk.Tk() #create the tkinter window
input_address = tk.Entry(root)
#input_address.pack(fill="both", expand=True)
input_address.pack(expand=True)
button_load = tk.Button(root,text='Go')
button_load.pack()

frame = HtmlFrame(root) #create HTML browser
frame.load_website("http://tkhtml.tcl.tk/tkhtml.html") #load a website
frame.pack(fill="both", expand=True) #attach the HtmlFrame widget to the parent window
root.mainloop()