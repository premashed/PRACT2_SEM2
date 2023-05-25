import socket
import pickle
import cryptocode

sock = socket.socket()
print('Please enter port: ')
port = int(input('> '))
sock.connect(('localhost', port))


def encrypt():
    p, g, A = pickle.loads(sock.recv(1024))
    b = 7
    B = g ** b % p
    sock.send(pickle.dumps(B))
    K = A ** b % p
    key = str(K)
    print('Enter your message: ')
    message = input('> ')
    encrypted = cryptocode.encrypt(message, key)
    sock.send(pickle.dumps(encrypted))
    return message


def decrypt():
    p, g, a = 7, 5, 3
    A = g ** a % p
    sock.send(pickle.dumps((p, g, A)))
    B = pickle.loads(sock.recv(1024))
    K = B ** a % p
    key = str(K)
    encrypted = pickle.loads(sock.recv(1024))
    print('Encrypted message:', encrypted)
    message = cryptocode.decrypt(encrypted, key)
    print('Decrypted message:', message)


while True:
    decrypt()
    message = encrypt()
    if message == 'exit':
        break
sock.close()
