#!/usr/bin/env python

# Luis Ramirez

# Python Socket Program
# This program is in beta testing
# server.py will listen to any message connection through client.py

# The Game xd
# Tengo hueva de hacer esto pero estaria chido cuando funcione todo bien

import socket
import threading

# Server info
PORT = 6423
SERVER_IP = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER_IP, PORT)

# Message handler
HEADER = 64
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

# Socket definition
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn, addr):
    print(f"Address {addr} connected.")
    
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode()
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f"[{addr}] {msg}")
            conn.send("RECEIVED".encode(FORMAT))
    conn.close()
    
    
def start():
    # Bruh
    server.listen()
    print(f"Server is listening on {SERVER_IP}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"Connections: {threading.activeCount() - 1}")

    
print("Server is running...")
start()

