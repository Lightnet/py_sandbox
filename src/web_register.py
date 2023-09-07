# https://stackoverflow.com/questions/2416486/how-to-create-a-password-entry-field-using-tkinter
# https://www.geeksforgeeks.org/python-tkinter-messagebox-widget/
# 
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
    #ALIAS
    label_alias = ttk.Label(text="Alias:")
    label_alias.grid(row=2,column=0)

    input_alias = ttk.Entry()
    input_alias.grid(row=2,column=1)
    self.input_alias = input_alias
    #PASS
    label_pass = ttk.Label(text="Pass:")
    label_pass.grid(row=3,column=0)

    input_pass = ttk.Entry(show="*")
    input_pass.grid(row=3,column=1)
    self.input_pass = input_pass

    label_pass02 = ttk.Label(text="RE-Pass:")
    label_pass02.grid(row=4,column=0)

    input_pass02 = ttk.Entry(show="*")
    input_pass02.grid(row=4,column=1)
    self.input_pass02 = input_pass02
    #EMAIL
    label_email = ttk.Label(text="Email:")
    label_email.grid(row=5,column=0)

    input_email = ttk.Entry()
    input_email.grid(row=5,column=1)
    self.input_email = input_email

    label_email02 = ttk.Label(text="RE-Email:")
    label_email02.grid(row=6,column=0)

    input_email02 = ttk.Entry()
    input_email02.grid(row=6,column=1)
    self.input_email02 = input_email02

    #BUTTONS
    frame_buttons = ttk.Frame()
    frame_buttons.grid(row=7,column=0,columnspan=2)

    #button_login = ttk.Button(frame_buttons,text='Login',bootstyle=(INFO, OUTLINE))
    #button_login.grid(row=0,column=0)

    button_create = ttk.Button(frame_buttons,text='Register',bootstyle=SUCCESS)
    button_create.grid(row=0,column=1)
    button_create['command'] = self.web_register

    button_Cancel = ttk.Button(frame_buttons,text='Cancel',bootstyle=WARNING)
    button_Cancel.grid(row=0,column=2)

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

if __name__ == '__main__':
  root = Tk()
  root.geometry("300x300")
  mail_gui = gui_register(root)
  root.mainloop()