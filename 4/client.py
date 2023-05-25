import socket
import threading
import time


def connect():
    global client
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 9093))
    return client


def send(client, msg):
    try:
        message = msg.encode()
        client.send(message)
    except ConnectionResetError:
        print("Your message was not delivered")


connection = connect()
print('Please enter your user name: ')
username = input('> ')

def receive():
    try:
        while True:
            print(client.recv(1024).decode())
    except ConnectionResetError:
        print('Connection has been reset')

thread = threading.Thread(target=receive)
thread.start()
print('You can chat now')
while True:
    msg = input("> ")
    if msg == 'exit':
        send(connection, username + ' has disconnected')
        break
    send(connection, username + ': ' + msg)
send(connection, 'exit')
time.sleep(1)
print('Successfully disconnected')
