# https://python-textbok.readthedocs.io/en/1.0/Introduction_to_GUI_Programming.html
# https://www.digitalocean.com/community/tutorials/tkinter-working-with-classes
#for gui mail to send mail server.

from tkinter import Tk, ttk, Text, Entry

class gui_mail:
  def __init__(self,master):
    self.master = master
    master.title("A simple GUI")

    text_box1 = Entry()
    text_box1.pack()

    text_box = Text()
    text_box.pack()    

if __name__ == '__main__':
  root = Tk()
  mail_gui = gui_mail(root)
  root.mainloop()