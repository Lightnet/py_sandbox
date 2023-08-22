import tkinter as tk
from tkinter import scrolledtext
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class MainWindow(tk.Tk):
  def __init__(self,*args, **kwargs):
    super().__init__(*args, **kwargs)

    #self.configure(background='black')#for debug layout
    
    #========================
    # FRAME
    frame_server = ttk.Frame(self)# FRAME
    frame_server.grid(row=0, column=0, columnspan=1, sticky=tk.W+tk.E)
    #frame_server.configure(background='black')#for debug layout
    # LABEL
    label_server = ttk.Label(frame_server, text="Server:")
    label_server.grid(row=0,column=0,sticky=tk.W+tk.E, pady=4, padx=4)
    # ENTRY
    input_server = ttk.Entry(frame_server)
    input_server.grid(row=0,column=1,sticky=tk.W+tk.E)
    # LABEL
    label_port = ttk.Label(frame_server, text="Port:")
    label_port.grid(row=0,column=2,sticky=tk.W+tk.E)
    # ENTRY
    input_port = ttk.Entry(frame_server,width=6)
    input_port.grid(row=0,column=3,sticky=tk.W+tk.E,padx=4)

    frame_server.columnconfigure(1, weight=1)
    #========================
    # FROM
    frame_from = ttk.Frame(self)# FRAME
    frame_from.grid(row=1, column=0, sticky=tk.W+tk.E, pady=4, padx=4)

    label_from = ttk.Label(frame_from, text="From:")
    label_from.grid(row=0,column=0,sticky=tk.W+tk.E)
    input_from = ttk.Entry(frame_from)
    input_from.grid(row=0,column=1,sticky=tk.W+tk.E)

    frame_from.columnconfigure(1, weight=1)
    #========================
    # TO
    frame_to = ttk.Frame(self)# FRAME
    frame_to.grid(row=2, column=0, sticky=tk.W+tk.E, pady=4, padx=4)

    label_to = ttk.Label(frame_to, text="To:")
    label_to.grid(row=0,column=0,sticky=tk.W+tk.E)

    input_to = ttk.Entry(frame_to)
    input_to.grid(row=0,column=1,sticky=tk.W+tk.E)
    frame_to.columnconfigure(1, weight=1)
    #========================
    # SUBJECT
    frame_subject = ttk.Frame(self)# FRAME
    frame_subject.grid(row=3, column=0, sticky=tk.W+tk.E, pady=4, padx=4)

    label_subject = ttk.Label(frame_subject, text="Subject:")
    label_subject.grid(row=0,column=0)

    input_subject = ttk.Entry(frame_subject)
    input_subject.grid(row=0,column=1,sticky=tk.W+tk.E)
    frame_subject.columnconfigure(1, weight=1)
    #========================
    # CONTENT
    frame_content = ttk.LabelFrame(self, text="Message")# FRAME
    frame_content.grid(row=4, column=0,columnspan=2, sticky=tk.E+tk.W+tk.N+tk.S, pady=4, padx=4)

    frame_content.rowconfigure(0, weight=1)
    frame_content.columnconfigure(0, weight=1)

    #========================
    # ACTIONS
    frame_actions = ttk.Frame(self)# FRAME
    frame_actions.grid(row=5, column=0, sticky=tk.E+tk.W, pady=4, padx=4)
    #frame_actions.configure(background='black')#for debug layout
    button_send = ttk.Button(frame_actions, text="Send")
    button_send.grid(row=0, column=1)

    button_draft = ttk.Button(frame_actions, text="Draft")
    button_draft.grid(row=0, column=0)


    #txtbox = ttk.scrolledtext.ScrolledText(frame_content, width=40, height=10)
    txtbox = ttk.ScrolledText(frame_content, width=40, height=10)
    txtbox.grid(row=0, column=0, sticky=tk.E+tk.W+tk.N+tk.S)

    # weight for auto layout adjust
    self.columnconfigure(0, weight=1) # input server
    # note repeat columnconfigure seem to break layout on right empty space when resize
    self.rowconfigure(4, weight=1) # content
    #self.columnconfigure(4, weight=1) # 

    #self.rowconfigure(5, weight=1) # Action
    #self.columnconfigure(4, weight=1) # message content

    self.grid_columnconfigure(0, weight=1)

  def connect_server(self):
    pass

  def disconnect_server(self):
    pass

if __name__ == '__main__':
  app = MainWindow()
  app.mainloop()