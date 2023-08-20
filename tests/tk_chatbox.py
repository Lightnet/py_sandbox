#simple message chat layout 

import tkinter as tk
from tkinter import scrolledtext

class MainWindow(tk.Tk):
  def __init__(self, screenName: str | None = None, baseName: str | None = None, className: str = "Tk", useTk: bool = True, sync: bool = False, use: str | None = None) -> None:
    super().__init__(screenName, baseName, className, useTk, sync, use)

    buttons_frame = tk.Frame(self)
    buttons_frame.grid(row=0, column=0, sticky=tk.W+tk.E)
    buttons_frame.configure(background='black')#for debug layout

    btn_Leave = tk.Button(buttons_frame, text='Leave')
    btn_Leave.grid(row=0, column=0, padx=8, pady=8)

    btn_Settings = tk.Button(buttons_frame, text='Settings')
    btn_Settings.grid(row=0, column=1, padx=8, pady=8)

    btn_Members= tk.Button(buttons_frame, text='Members')
    btn_Members.grid(row=0, column=2, padx=8, pady=8)

    # Chat Message ----------------------------------------------------
    group1 = tk.LabelFrame(self, text="Chat Message", padx=5, pady=5)
    #group1.configure(background='black')#for debug layout
    group1.grid(row=1, column=0, columnspan=2, padx=8, pady=8, sticky=tk.E+tk.W+tk.N+tk.S)

    # chat user frame
    chat_frame = tk.Frame(self)
    chat_frame.grid(row=2, column=0, sticky=tk.W+tk.E)    
    #chat_frame.configure(background='black')#for debug layout
    # chat input
    input_message = tk.Entry(chat_frame)
    input_message.grid(row=0, column=0, padx=(8), pady=8,sticky=tk.W+tk.E)
    input_message.bind('<Return>', self.input_chat)
    btn_send = tk.Button(chat_frame, text='Send')
    btn_send.grid(row=0, column=1, padx=(8), pady=8)

    chat_frame.columnconfigure(0, weight=1)# Entry chat input, need to place here
    
    # weight for auto layout adjust
    self.columnconfigure(0, weight=1) #buttons
    self.rowconfigure(1, weight=1)#chat message
    self.columnconfigure(2, weight=1)#chat input
    #self.rowconfigure(2, weight=1)#chat input , nope effect fixed
    
    group1.rowconfigure(0, weight=1)
    group1.columnconfigure(0, weight=1)

    # Create the textbox
    txtbox = scrolledtext.ScrolledText(group1, width=40, height=10)
    txtbox.grid(row=0, column=0, sticky=tk.E+tk.W+tk.N+tk.S)

  def input_chat(self,event):
    print("Hello test")
    pass
if __name__ == '__main__':
  app = MainWindow()
  app.mainloop()