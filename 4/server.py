import socket
import threading
from datetime import datetime


def check_credentials(username, password):
    with open('pass.txt', 'r') as file:
        for line in file:
            stored_username, stored_password = line.strip().split()
            if username == stored_username and password == stored_password:
                return True
    return False


def handle_client(conn, addr):
    auth = False
    print('New connection {}'.format(addr))
    log = open('log.txt', 'a+')
    log.write('New connection {}'.format(addr))
    log.write(' at {}\n'.format(datetime.now()))

    # Authentication process
    while not auth:
        credentials = conn.recv(1024).decode().split()
        username = credentials[0]
        password = credentials[1]

        if check_credentials(username, password):
            auth = True
            conn.sendall(b'Authorized')
            users_list[addr] = username
            print('{} has been authorized'.format(username))
        else:
            conn.sendall(b'Unauthorized')
            print('{} failed to authenticate'.format(username))

    try:
        while True:
            message = conn.recv(1024).decode()
            if not message:
                log.close()
                break
            if message != 'exit':
                username = message[:message.index(':')]
                print(message)
                log.write(message)
                log.write(' at {}\n'.format(datetime.now()))
            if message == 'exit':
                username = message[:message.index(':')]
                log.write('{} has disconnected'.format(username))
                log.write(' at {}\n'.format(datetime.now()))
                print(username, 'has disconnected')
            with clients_lock:
                for client in clients:
                    if client != conn:
                        client.sendall(message.encode())

    except:
        clients.remove(conn)
        conn.close()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 9097))

clients = set()
clients_lock = threading.Lock()
users_list = {}

server.listen()

while True:
    conn, addr = server.accept()
    with clients_lock:
        clients.add(conn)
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()
