from socket import *
import socket

import sqlite3
import numpy as np

'''
def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 54000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    message = input(" -> ")  # take input

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response

        print('Received from server: ' + data)  # show in terminal

        message = input(" -> ")  # again take input

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()
'''
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 54000))
client.send("I am CLIENT<br>".encode())
from_server = client.recv(4096).decode()
client.close()
print (from_server)

'''
def viewData():
    con = sqlite3.connect("foodmanagement.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM foodmanagement")
    rows = cur.fetchall()
    con.close
    return rows

'''
