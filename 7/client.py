import socket


currentDirectory = ''
print('Please use one of the following commands: ')
print('makefile <filename>, writefile <filename> <content>, readfile <filename>, delfile <filename>, quit')
while True:
    request = input('{}>'.format(currentDirectory))
    sock = socket.socket()
    sock.connect(('localhost', 8080))
    sock.send(request.encode())
    response = sock.recv(1024).decode()
    print(response)
    sock.close()
    if request == 'quit':
        break