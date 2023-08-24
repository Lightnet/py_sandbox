#simple message chat layout 
# https://copyassignment.com/gui-chat-application-in-python-tkinter/
# 
# 
# 
# 
# https://www.youtube.com/watch?v=D0SLpD7JvZI Simple Python Chat Server
# 
# 


import tkinter as tk
from tkinter import END, scrolledtext
import socket
import threading


class ChatServer:
  client_list = []
  last_received_message  = ""

  def __init__(self):
    self.server_socket = None
    self.create_listening_server()

  #listen for incoming connection
  def create_listening_server(self):
    self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create a socket using TCP port and ipv4
    local_ip = '127.0.0.1'
    local_port = 10319
    # this will allow you to immediately restart a TCP server
    self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # this makes the server listen to requests coming from other computers on the network
    self.server_socket.bind((local_ip, local_port))
    print("Listening for incoming messages..")
    self.server_socket.listen(5) #listen for incomming connections / max 5 clients
    self.receive_messages_in_a_new_thread()

  #fun to receive new msgs
  def receive_messages(self, so):
    while True:
      incoming_buffer = so.recv(256) #initialize the buffer
      if not incoming_buffer:
        break
      self.last_received_message = incoming_buffer.decode('utf-8')
      self.broadcast_to_all_clients(so)  # send to all clients
    so.close()
  #broadcast the message to all clients 
  def broadcast_to_all_clients(self, senders_socket):
    for client in self.clients_list:
      socket, (ip, port) = client
      if socket is not senders_socket:
        socket.sendall(self.last_received_message.encode('utf-8'))

  def receive_messages_in_a_new_thread(self):
    while True:
      client = so, (ip, port) = self.server_socket.accept()
      self.add_to_clients_list(client)
      print('Connected to ', ip, ':', str(port))
      t = threading.Thread(target=self.receive_messages, args=(so,))
      t.start()
  #add a new client 
  def add_to_clients_list(self, client):
    if client not in self.clients_list:
      self.clients_list.append(client)


class MainWindow(tk.Tk):
  def __init__(self, screenName: str | None = None, baseName: str | None = None, className: str = "Tk", useTk: bool = True, sync: bool = False, use: str | None = None) -> None:
    super().__init__(screenName, baseName, className, useTk, sync, use)
    self.HOST = "127.0.0.1"
    self.PORT = 1023

    buttons_frame = tk.Frame(self)
    buttons_frame.grid(row=0, column=0, sticky=tk.W+tk.E)
    #buttons_frame.configure(background='black')#for debug layout

    btn_Leave = tk.Button(buttons_frame, text='Leave')
    btn_Leave.grid(row=0, column=0, padx=8, pady=8)

    btn_Settings = tk.Button(buttons_frame, text='Settings')
    btn_Settings.grid(row=0, column=1, padx=8, pady=8)

    btn_Members= tk.Button(buttons_frame, text='Members')
    btn_Members.grid(row=0, column=2, padx=8, pady=8)

    btn_server= tk.Button(buttons_frame, text='server')
    btn_server.grid(row=0, column=3, padx=8, pady=8)
    btn_server['command'] = self.init_server

    btn_client= tk.Button(buttons_frame, text='client')
    btn_client.grid(row=0, column=4, padx=8, pady=8)
    btn_client['command'] = self.init_client
    #============================================
    # Chat Messages
    frame_messages = tk.LabelFrame(self, text="Chat Message", padx=5, pady=5)
    #group1.configure(background='black')#for debug layout
    frame_messages.grid(row=1, column=0, columnspan=2, padx=8, pady=8, sticky=tk.E+tk.W+tk.N+tk.S)

    frame_messages.rowconfigure(0, weight=1)
    frame_messages.columnconfigure(0, weight=1)

    # Create the textbox scroll
    txtbox = scrolledtext.ScrolledText(frame_messages, width=40, height=10)
    txtbox.grid(row=0, column=0, sticky=tk.E+tk.W+tk.N+tk.S)
    #============================================
    # Frame Chat Input
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

  def init_server(self):
    print("init server test")
    
  def init_client(self):
    print("init client test")
  # https://copyassignment.com/gui-chat-application-in-python-tkinter/
  def setup_client(self):
    self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # initialazing socket with TCP and IPv4
    remote_ip = '127.0.0.1' # IP address 
    remote_port = 10319 #TCP port
    self.client_socket.connect((remote_ip, remote_port))#connect to the remote server

  def listen_for_incoming_messages_in_a_thread(self):
    thread = threading.Thread(target=self.receive_message_from_server, args=(self.client_socket,)) # Create a thread for the send and receive in same time 
    thread.start()

  #function to recieve msg
  def receive_message_from_server(self, so):
    while True:
      buffer = so.recv(256)
      if not buffer:
        break
      message = buffer.decode('utf-8')
   
      if "joined" in message:
        user = message.split(":")[1]
        message = user + " has joined"
        print("")
        #self.chat_transcript_area.insert('end', message + '\n')
        #self.chat_transcript_area.yview(END)
      else:
        print("")
        #self.chat_transcript_area.insert('end', message + '\n')
        #self.chat_transcript_area.yview(END)

      so.close()
  def input_chat(self,event):
    print("Hello test")

if __name__ == '__main__':
  app = MainWindow()
  app.mainloop()