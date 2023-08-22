import tkinter as tk
from tkinter import scrolledtext
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class MainWindow(tk.Tk):
  def __init__(self,*args, **kwargs):
    super().__init__(*args, **kwargs)

  def init_mailbox(self):
    
    pass

  def open_mail():
    print("")

  def refresh_mail(self):
    pass

  def mark_read_mail(self):
    pass

  def mark_unread_mail(self):
    pass

  def delete_mail(self):
    pass

if __name__ == '__main__':
  app = MainWindow()
  app.mainloop()