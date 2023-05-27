import socket


currentDirectory = ''
print('Please use one of the following commands: ')
print('make <filename>, write <filename> <content>, read <filename>, delete<filename>, quit')
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
