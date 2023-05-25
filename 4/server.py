import socket
import threading
from datetime import datetime
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 9093))

clients = set()
clients_lock = threading.Lock()


def handle_client(conn, addr):
    print('New connection {}'.format(addr))
    log = open('log.txt', 'a+')
    log.write('New connection {}'.format(addr))
    log.write(' at {}\n'.format(datetime.now()))
    try:
        while True:
            message = conn.recv(1024).decode()
            if not message:
                log.close()
                break
            if message != 'exit':
                username = message[:message.index(':')]
                users_list[addr] = username
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


server.listen()
users_list = {}
while True:
    conn, addr = server.accept()
    with clients_lock:
        clients.add(conn)
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()
