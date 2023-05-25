import socket
import pickle
import cryptocode
import psutil

sock = socket.socket()
port = 9090
while port in [i.laddr.port for i in psutil.net_connections()]:
    port += 1
    print('new port', port)
sock.bind(('', port))
sock.listen(1)
conn, addr = sock.accept()
def decrypt():
    p, g, A = pickle.loads((conn.recv(1024)))
    b = 7
    B = g ** b % p
    conn.send(pickle.dumps(B))
    K = A ** b % p
    key = str(K)
    print('Enter your message: ')
    message = input('> ')
    decrypted = cryptocode.encrypt(message, key)
    conn.send(pickle.dumps(decrypted))
def encrypt():
    p, g, a = 7, 5, 3
    A = g ** a % p
    conn.send(pickle.dumps((p, g, A)))
    B = pickle.loads(conn.recv(1024))
    K = B ** a % p
    key = str(K)
    encrypted = pickle.loads(conn.recv(1024))
    print('Encrypted message:', encrypted)
    message = cryptocode.decrypt(encrypted, key)
    print('Decrypted message:', message)
    return message

while True:
    decrypt()
    message = encrypt()
    if message == 'exit':
        break
conn.close()
