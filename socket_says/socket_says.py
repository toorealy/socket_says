#!/bin/python

# Socket Says - Because abstraction is fun

from abc import ABC
import atexit
from socket import *
import sys

from ipaddress import ip_address

from .custom_errors import BadPortError,\
                          BadAddressError


class SocketSays(ABC):
    def __init__(self, /,address='127.0.0.1', port=80):
        self.address = address
        self.port = port
        self.text = 'Hello'
        self.socket = self.establish_socket()
        atexit.register(self.close_socket)

    def __len__(self):
        return len(self.text)

    def __str__(self):
        return "You are telling {} on port {} '{}'".format(self.address,
                                                           self.port,
                                                           self.text)

    def __repr__(self):
        return "<SocketSays({},{},{})>".format(self.address,
                                               self.port,
                                               self.text)

    def format_text(self, text="", special=None):
        return text.encode()  # this should become more robust as we add base64, hex, etc.

    def says(self, text="Hello", *, special=None, return_size=450):
        """ Creates SocketSays' ability to speak on the socket"""
        self.text = text
        for line in self.text.splitlines():
            self.volley(self.format_text(line + '\n', special), return_size)

    def listens(self, socket):
        """ Creates SocketSays' ability to receive on the socket"""
        print(socket.recv(2048*multiple))

    def volley(self, text: str, multiple: int = 450):
        self.socket.send(text)

    def close_socket(self):
        try:
            self.socket.close()
        except AttributeError:
            pass

    def establish_socket(self, *, old_socket=None):
        if old_socket:
            self.close_socket()
        new_socket = socket(AF_INET, SOCK_STREAM)
        try:
            new_socket.connect((str(self.address), self.port))
            return new_socket
        except ConnectionRefusedError:
            print("I'm sorry. The connection was refused")
            return None  # will want this to be a fatal error

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, val):
        try:
            self._address = ip_address(val)
        except ValueError as e:
            raise BadAddressError(e)

    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, val):
        try:
            self._port = int(val)
        except ValueError as e:
            raise BadPortError(e)
