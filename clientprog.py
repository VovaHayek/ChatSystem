import socket
import threading

alias = input('Choose an alias >>> ')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 8080
client.connect((host, port))

def client_recieve():
	while True:
		try:
			message = client.recv(1024).decode()
			if message == 'alias?':
				client.send(alias.encode())
			else:
				print(message)
		except:
			print('ERROR')
			client.close()
			break

def client_send():
	while True:
		message = f'{alias}: {input("")}'
		client.send(message.encode())

recieve_thread = threading.Thread(target = client_recieve)
recieve_thread.start()

send_thread = threading.Thread(target = client_send)
send_thread.start()
