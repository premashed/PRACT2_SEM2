import socket
import os


def process(command, req):
    print(command, req)
    if req != [] and command != 'quit':
        if command == 'make':
            return create_file(rootDirectory, req[0])
        elif command == 'write':
            return write_file(rootDirectory, req[0], req[1:])
        elif command == 'read':
            return read_file(rootDirectory, req[0])
        elif command == 'delete':
            return delete_file(rootDirectory, req[0])
        elif command == 'quit':
            return 'Connection has been reset'
    else:
        return 'Unknown command'


def create_file(path, name):
    filename = os.path.join(path, name)
    if not os.path.exists(filename):
        open(filename, 'a').close()
        return 'Successfully created file'
    else:
        return 'File already exists'


def write_file(path, name, words):
    filename = os.path.join(path, name)
    file = open(filename, 'a')
    text = ''
    for word in words:
        text += str(word) + ' '
    file.write(text)
    file.close()
    return 'Text added successfully'


def read_file(path, name):
    filename = os.path.join(path, name)
    if os.path.exists(filename):
        file = open(filename, 'r')
        text = file.read()
        file.close()
        return text
    else:
        return 'File does not exist'


def delete_file(path, name):
    filename = os.path.join(path, name)
    if os.path.exists(filename):
        os.remove(filename)
        return 'Deletion complete'
    else:
        return 'File does not exist'


rootDirectory = os.path.dirname(os.path.abspath(__file__))
dirName = 'root'
rootDirectory = os.path.join(rootDirectory, dirName)
if not os.path.exists(rootDirectory):
    os.mkdir(rootDirectory)

sock = socket.socket()
sock.bind(('', 8080))
sock.listen(1)
print('Server successfully started')
while True:
    conn, addr = sock.accept()
    request = conn.recv(1024).decode()
    print(request)
    request = request.split()
    command = request[0]
    del request[0]
    response = process(command, request)
    print(response)
    conn.send(response.encode())
    if request == 'quit':
        break

conn.close()
