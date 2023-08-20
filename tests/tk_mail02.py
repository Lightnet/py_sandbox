import tkinter as tk
from tkinter import scrolledtext

class MainWindow(tk.Tk):
  def __init__(self,*args, **kwargs):
    super().__init__(*args, **kwargs)


    frame_server = tk.Frame(self)# FRAME
    frame_server.grid(row=0, column=0, sticky=tk.W+tk.E)
    label_server = tk.Label(frame_server, text="Server:")
    label_server.grid(row=0,column=0,sticky=tk.W+tk.E)

    frame_from = tk.Frame(self)# FRAME
    frame_from.grid(row=1, column=0, sticky=tk.W+tk.E)
    label_from = tk.Label(frame_from, text="From:")
    label_from.grid(row=0,column=0,sticky=tk.W+tk.E)

    frame_to = tk.Frame(self)# FRAME
    frame_to.grid(row=2, column=0, sticky=tk.W+tk.E)
    label_to = tk.Label(frame_to, text="To:")
    label_to.grid(row=0,column=0,sticky=tk.W+tk.E)

    frame_subject = tk.Frame(self)# FRAME
    frame_subject.grid(row=3, column=0, sticky=tk.W+tk.E)
    label_subject = tk.Label(frame_subject, text="Subject:")
    label_subject.grid(row=0,column=0,sticky=tk.W+tk.E)
    

    # Group1 Frame ----------------------------------------------------
    group1 = tk.LabelFrame(self, text="Message", padx=5, pady=5)
    group1.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky=tk.E+tk.W+tk.N+tk.S)
    group1.rowconfigure(0, weight=1)
    group1.columnconfigure(0, weight=1)

    frame_from = tk.Frame(self)# FRAME
    frame_from.grid(row=5, column=0, sticky=tk.W+tk.E)
    label_from = tk.Label(frame_from, text="Actions:")
    label_from.grid(row=0,column=0,sticky=tk.W+tk.E)


    self.columnconfigure(0, weight=1)
    self.columnconfigure(1, weight=1)
    self.rowconfigure(4, weight=1)
    #self.columnconfigure(3, weight=1)

    

    # Create the textbox
    txtbox = scrolledtext.ScrolledText(group1, width=40, height=10)
    txtbox.grid(row=0, column=0, sticky=tk.E+tk.W+tk.N+tk.S)
    
  def connect_server(self):
    pass

  def disconnect_server(self):
    pass

if __name__ == '__main__':
  app = MainWindow()
  app.mainloop()