
# 
"""
  For Admin set up for database.
"""

from tkinter import Tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
#from tkinter import messagebox
from ttkbootstrap.dialogs.dialogs import Messagebox

from alchemy.models import engine, User
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy import exc

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

    #DATABASE
    label_db = ttk.Label(text="Database:")
    label_db.grid(row=2,column=0)

    input_db = ttk.Entry()
    input_db.insert(END, 'database.sqlite')
    input_db.grid(row=2,column=1)
    #ALIAS
    label_alias = ttk.Label(text="Alias:")
    label_alias.grid(row=3,column=0)

    input_alias = ttk.Entry()
    input_alias.grid(row=3,column=1)
    self.input_alias = input_alias
    #PASS
    label_pass = ttk.Label(text="Pass:")
    label_pass.grid(row=4,column=0)

    input_pass = ttk.Entry(show="*")
    input_pass.grid(row=4,column=1)
    self.input_pass = input_pass
    #BUTTONS
    frame_buttons = ttk.Frame()
    frame_buttons.grid(row=5,column=0,columnspan=2)

    #button_forgot = ttk.Button(frame_buttons,text='Forgot',bootstyle=(INFO, OUTLINE))
    #button_forgot.grid(row=0,column=0)

    button_create = ttk.Button(frame_buttons,text='Create',bootstyle=SUCCESS)
    button_create.grid(row=0,column=1)
    button_create['command'] = self.web_register

    button_Cancel = ttk.Button(frame_buttons,text='Delete',bootstyle=WARNING)
    button_Cancel.grid(row=0,column=2)
    button_Cancel['command'] = self.web_delete

  def web_register(self):
    #messagebox.showinfo("showinfo", "Information")
    #Messagebox.ok("Hello World!")
    user_name = self.input_alias.get()
    passphrase = self.input_pass.get()
    print("user_name: ", user_name)
    print("passphrase: ", passphrase)

    try:
      with Session(engine) as session:
        result = session.execute(select(User).where(User.alias == user_name)).scalar()# if nothing return None
      print("RESULT: ", result)
      if result:
        print("FOUND")
        print("USER:", result)
        print("USER:", result.id)
        Messagebox.ok(f'User Found! {result.alias}!')
      else:
        newUser = User(
          alias = user_name,
          passphrase = passphrase
        )
        session.add_all([newUser])
        session.commit()
        print("ID: ", newUser.id)
        Messagebox.ok(f'Created Alias:[ {user_name} ]!')

    except exc.SQLAlchemyError as e:
      print("USER SIGN IN ERROR!", e)

  def web_delete(self):

    pass

if __name__ == '__main__':
  root = Tk()
  root.geometry("200x200")
  mail_gui = gui_register(root)
  root.mainloop()