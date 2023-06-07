import socket
import threading
import sys
import time


def connect():
    global client
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 9097))
    return client


def send(client, msg):
    try:
        message = msg.encode()
        client.send(message)
    except ConnectionResetError:
        print("Your message was not delivered")


def receive():
    try:
        while True:
            print(client.recv(1024).decode())
    except ConnectionResetError:
        print('Connection has been reset')


def authenticate(username, password):
    # Send credentials to server
    message = '{} {}'.format(username, password)
    send(connection, message)

    # Receive authentication response
    response = connection.recv(1024).decode()
    if response == 'Authorized':
        print('You are authorized')
    else:
        print('Authentication failed')
        connection.close()
        sys.exit(1)


def send_messages():
    while True:
        msg = input("> ")
        if msg == 'exit':
            send(connection, username + ' has disconnected')
            break
        send(connection, username + ': ' + msg)

    send(connection, 'exit')
    time.sleep(1)
    print('Successfully disconnected')


connection = connect()
print('Please enter your username: ')
username = input('> ')
print('Please enter your password: ')
password = input('> ')
authenticate(username, password)

receive_thread = threading.Thread(target=receive)
receive_thread.start()

send_thread = threading.Thread(target=send_messages)
send_thread.start()
