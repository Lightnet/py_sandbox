import tkinter as tk
from tkinter import scrolledtext

class MainWindow(tk.Tk):
  def __init__(self,*args, **kwargs):
    super().__init__(*args, **kwargs)
    # Group1 Frame ----------------------------------------------------
    group1 = tk.LabelFrame(self, text="Text Box", padx=5, pady=5)
    group1.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky=tk.E+tk.W+tk.N+tk.S)
    
    self.columnconfigure(0, weight=1)
    self.rowconfigure(1, weight=1)

    group1.rowconfigure(0, weight=1)
    group1.columnconfigure(0, weight=1)

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