import socket

sock = socket.socket()
print('Please enter your username: ')
username = input('> ')
print('Please enter your password: ')
password = input('> ')
print('Please enter desired port: ')
port = input('> ')
port, ipaddr = int(port), 'localhost'

sock.connect((ipaddr, port))
sock.send((username + ' ' + password).encode())

welc = sock.recv(1024).decode()
print(welc)

while True:
    data = input('{}>'.format(username))
    sock.send(data.encode())
    if data == 'exit':
        break
    else:
        reply = sock.recv(1024).decode()
        print('Server: {}'.format(reply))
    
sock.close()
