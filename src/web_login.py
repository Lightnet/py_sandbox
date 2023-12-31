
# 

from tkinter import Tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
#from tkinter import messagebox
from ttkbootstrap.dialogs.dialogs import Messagebox

class gui_register(ttk.Frame):
  def __init__(self,master):
    self.master = master

    master.title("A simple GUI")
    #ADDRESS
    label_address = ttk.Label(text="Address:")
    label_address.grid(row=0,column=0)

    input_address = ttk.Entry()
    input_address.insert(END, 'localhost')
    input_address.grid(row=0,column=1)
    #PORT
    label_port = ttk.Label(text="Port:")
    label_port.grid(row=1,column=0)

    input_port = ttk.Entry()
    input_port.insert(END, '3000')
    input_port.grid(row=1,column=1)
    #ALIAS
    label_alias = ttk.Label(text="Alias:")
    label_alias.grid(row=2,column=0)

    input_alias = ttk.Entry()
    input_alias.grid(row=2,column=1)
    #PASS
    label_pass = ttk.Label(text="Pass:")
    label_pass.grid(row=3,column=0)

    input_pass = ttk.Entry(show="*")
    input_pass.grid(row=3,column=1)
    #BUTTONS
    frame_buttons = ttk.Frame()
    frame_buttons.grid(row=4,column=0,columnspan=2)

    #button_forgot = ttk.Button(frame_buttons,text='Forgot',bootstyle=(INFO, OUTLINE))
    #button_forgot.grid(row=0,column=0)

    button_create = ttk.Button(frame_buttons,text='Login',bootstyle=SUCCESS)
    button_create.grid(row=0,column=1)
    button_create['command'] = self.web_register

    button_Cancel = ttk.Button(frame_buttons,text='Cancel',bootstyle=WARNING)
    button_Cancel.grid(row=0,column=2)

  def web_register(self):
    #messagebox.showinfo("showinfo", "Information")
    Messagebox.ok("Hello World!")

if __name__ == '__main__':
  root = Tk()
  root.geometry("200x200")
  mail_gui = gui_register(root)
  root.mainloop()