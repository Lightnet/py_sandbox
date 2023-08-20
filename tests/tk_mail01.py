import tkinter as tk
from tkinter import scrolledtext

class MainWindow(tk.Tk):
  def __init__(self,*args, **kwargs):
    super().__init__(*args, **kwargs)

    self.configure(background='black')#for debug layou
    
    #========================
    # FRAME
    frame_server = tk.Frame(self)# FRAME
    frame_server.grid(row=0, column=0, columnspan=1, sticky=tk.W+tk.E)
    #frame_server.configure(background='black')#for debug layout
    # LABEL
    label_server = tk.Label(frame_server, text="Server:")
    label_server.grid(row=0,column=0,sticky=tk.W+tk.E)
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
    # FROM
    frame_from = tk.Frame(self)# FRAME
    frame_from.grid(row=1, column=0, sticky=tk.W+tk.E)

    label_from = tk.Label(frame_from, text="From:")
    label_from.grid(row=0,column=0,sticky=tk.W+tk.E)
    input_from = tk.Entry(frame_from)
    input_from.grid(row=0,column=1,sticky=tk.W+tk.E)

    frame_from.columnconfigure(1, weight=1)
    #========================
    # TO
    frame_to = tk.Frame(self)# FRAME
    frame_to.grid(row=2, column=0, sticky=tk.W+tk.E)

    label_to = tk.Label(frame_to, text="To:")
    label_to.grid(row=0,column=0,sticky=tk.W+tk.E)

    input_to = tk.Entry(frame_to)
    input_to.grid(row=0,column=1,sticky=tk.W+tk.E)
    frame_to.columnconfigure(1, weight=1)
    #========================
    # SUBJECT
    frame_subject = tk.Frame(self)# FRAME
    frame_subject.grid(row=3, column=0, sticky=tk.W+tk.E)

    label_subject = tk.Label(frame_subject, text="Subject:")
    label_subject.grid(row=0,column=0)

    input_subject = tk.Entry(frame_subject)
    input_subject.grid(row=0,column=1,sticky=tk.W+tk.E)
    frame_subject.columnconfigure(1, weight=1)
    #========================
    # CONTENT
    frame_content = tk.LabelFrame(self, text="Message")# FRAME
    frame_content.grid(row=4, column=0,columnspan=2, sticky=tk.E+tk.W+tk.N+tk.S)

    frame_content.rowconfigure(0, weight=1)
    frame_content.columnconfigure(0, weight=1)

    #========================
    # ACTIONS
    frame_actions = tk.Frame(self)# FRAME
    frame_actions.grid(row=5, column=0, sticky=tk.E+tk.W)
    frame_actions.configure(background='black')#for debug layout
    button_send = tk.Button(frame_actions, text="Send")
    button_send.grid(row=0, column=0)


    txtbox = scrolledtext.ScrolledText(frame_content, width=40, height=10)
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