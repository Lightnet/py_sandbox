# test call

import tkinter as tk
from tkinter import scrolledtext

class MainWindow(tk.Tk):
  def __init__(self,*args, **kwargs):
    super().__init__(*args, **kwargs)

    #self.configure(background='black')#for debug layout
    
    #========================
    # FRAME
    frame_server = tk.Frame(self)# FRAME
    frame_server.grid(row=0, column=0, columnspan=1, sticky=tk.W+tk.E)
    #frame_server.configure(background='black')#for debug layout
    # LABEL
    label_server = tk.Label(frame_server, text="Server:")
    label_server.grid(row=0,column=0,sticky=tk.W+tk.E, pady=4, padx=4)
    # ENTRY
    input_server = tk.Entry(frame_server)
    input_server.grid(row=0,column=1,sticky=tk.W+tk.E)
    # LABEL
    label_port = tk.Label(frame_server, text="Port:")
    label_port.grid(row=0,column=2,sticky=tk.W+tk.E)
    # ENTRY
    input_port = tk.Entry(frame_server,width=6)
    input_port.grid(row=0,column=3,sticky=tk.W+tk.E)

    frame_server.columnconfigure(1, weight=1)
    #========================

    #========================
    # CONTENT
    frame_content = tk.LabelFrame(self, text="Message")# FRAME
    frame_content.grid(row=4, column=0,columnspan=2, sticky=tk.E+tk.W+tk.N+tk.S, pady=4, padx=4)

    frame_content.rowconfigure(0, weight=1)
    frame_content.columnconfigure(0, weight=1)

    #========================
    # ACTIONS
    frame_actions = tk.Frame(self)# FRAME
    frame_actions.grid(row=5, column=0, sticky=tk.E+tk.W, pady=4, padx=4)
    #frame_actions.configure(background='black')#for debug layout
    button_ping = tk.Button(frame_actions, text="Ping")
    button_ping.grid(row=0, column=1)

    button_draft = tk.Button(frame_actions, text="Draft")
    button_draft.grid(row=0, column=0)

    button_connect = tk.Button(frame_actions, text="Connect")
    button_connect.grid(row=0, column=2)


    txtbox = scrolledtext.ScrolledText(frame_content, width=40, height=10)
    txtbox.grid(row=0, column=0, sticky=tk.E+tk.W+tk.N+tk.S)

    # weight for auto layout adjust
    self.columnconfigure(0, weight=1) # input server
    # note repeat columnconfigure seem to break layout on right empty space when resize
    self.rowconfigure(4, weight=1) # content

    self.grid_columnconfigure(0, weight=1)

  def connect_server(self):
    pass

  def disconnect_server(self):
    pass

if __name__ == '__main__':
  app = MainWindow()
  app.mainloop()