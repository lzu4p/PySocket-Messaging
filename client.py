#!/usr/bin/env python

# Luis Ramirez

# 

import socket

# Client info
PORT = 6423
SERVER = "25.9.167.17"
ADDR = (SERVER, PORT)

# Message handler
HEADER = 64
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

CLIENT = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
CLIENT.connect(ADDR)


def send(message):
    msg = message.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b" " * (HEADER - len(send_length))
    CLIENT.send(send_length)
    CLIENT.send(msg)
    print(CLIENT.recv(2048).decode(FORMAT))

send("The Game")
input()
send("Wenas a todos putas zorras xd")
input()
send("Send nudes")
input()
send(DISCONNECT_MESSAGE)
