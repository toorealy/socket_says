#!/bin/python

# Socket Says - Because abstraction is fun

from abc import ABC
from socket import *
import sys

class SocketSays(ABC):
    def __init__(self, address='127.0.0.1', port=80):
        self.address = address
        self.port = port
        self.text = 'Hello'

    def __str__(self):
        return "You are telling {} on port {} '{}'".format(self.address,
                                                           self.port,
                                                           self.text)

    def __repr__(self):
        return "<SocketSays({},{},{})>".format(self.address,
                                               self.port,
                                               self.text)

    def format_text(self, text="", special=None):
        print('formatting text')
        return text.encode()  # this should become more robust as we add base64, hex, etc.

    def says(self, text="Hello", *, special=None, return_size=450):
        self.text = text
        s = socket(AF_INET, SOCK_STREAM)
        try:
            s.connect((self.address, self.port))
        except ConnectionRefusedError:
            print("I'm sorry. The connection was refused")
        for line in self.text.splitlines():
            self.volley(s, self.format_text(line + '\n', special), return_size)
        s.close()

    def volley(self, socket: socket, text: str, multiple: int = 450):
        socket.send(text)
        #print(socket.recv(2048*multiple))
