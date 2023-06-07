import socket
import threading

N = 2**16 - 1
def scanner(ip, port):
	scan = socket.socket()

	try:
		connection = scan.connect((ip, port))
		print(f'Port {port} open')
		connection.close()
	except:
		pass

ip = input('Enter IP')

for i in range(N):
	thread = threading.Thread(target=scanner, args=(ip, i))
	thread.start()