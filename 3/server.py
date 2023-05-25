from datetime import datetime
import socket
import psutil


log = open('log.txt', 'a')
sock, port = socket.socket(), 9091
while port in [i.laddr.port for i in psutil.net_connections()]:
    port += 1
    print('new port', port)
sock.bind(('', port))
sock.listen(1)
log.write('Server started at {}\n'.format(datetime.now()))
conn, addr = sock.accept()
log.write('Connection attempt by {} at {}\n'.format(addr[0], datetime.now()))
username, password = (conn.recv(1024).decode()).split()
log.write('{} tried to log in '.format(username))
log.write('at {}\n'.format(username, datetime.now))

welc = ''
auth, userFound = False, False
users_list = open('users.txt', 'r')
for row in users_list:
    row = row.strip('\n').split()
    if row[0] == username:
        userFound = True
        welc = 'Welcome to the server, {}!'.format(username)
        if row[1] == password:
            auth = True
            break
        else:
            welc = 'Wrong password!\n'
            break

if not userFound:
    welc += 'You are not in the database! Please check your credentials\n'
    log.write('{} tried to connect'.format(username))
    log.write(' at {}\n'.format(datetime.now()))

if auth:
    log.write('{} successfully logged in'.format(username))
    log.write(' at {}\n'.format(datetime.now()))
    conn.send(welc.encode())
    log.write('Server: ' + welc)
    log.write(' at {}\n'.format(datetime.now()))
    while True:
        data = conn.recv(1024).decode()
        print('{}: {}'.format(username, data))
        log.write('{}: '.format(username))
        log.write(data + ' at {}\n'.format(datetime.now()))
        if data == 'quit':
            log.write('{} disconnected at {}\n'.format(username, datetime.now()))
            break
        elif data == 'time':
            message = str(datetime.now())
            conn.send(message.encode())
            log.write('Server: ' + message + ' at {}\n'.format(datetime.now()))
        elif data == 'whoami':
            message = username
            conn.send(message.encode())
            log.write('Server: ' + message + ' at {}\n'.format(datetime.now()))
        else:
            print('Please enter message:')
            message = input('> ')
            conn.send(message.encode())
            log.write('Server: ' + message + ' at {}\n'.format(datetime.now()))
else:
    log.write('Authentication attempt failed at {}\n'.format(datetime.now()))
    conn.send(welc.encode())
    log.write('Server: ' + welc + ' at\n'.format(datetime.now()))


log.write('Server closed at {}\n'.format(datetime.now()))
log.close()
conn.close()
