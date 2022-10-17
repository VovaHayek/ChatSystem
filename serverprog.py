import socket
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 8080
sock.bind(('', port))
print('Server\'s active and waiting for connections...')
sock.listen()

clients = []
aliases = []

def brodcast(msg):
	for client in clients:
		client.send(msg)

def handle_client(client):
	while True:
		try:
			message = client.recv(1024)
			brodcast(message)
		except:
			index = clients.index(client)
			clients.remove(client)
			client.close()
			alias = aliases[index]
			brodcast(f'{alias} has left the chat room'.encode())
			aliases.remove(alias)
			break

#Main function to recieve clients
def recieve():
	while True:
		print('Server running and listening...')
		client, address = sock.accept()
		print(f'Connection is established with {str(address)}')
		client.send('alias?'.encode())
		alias = client.recv(1024)
		aliases.append(alias)
		clients.append(client)
		print(f'The alias of the client is {alias}')
		brodcast(f'{alias} has joined chat room'.encode())
		client.send('You are now connected!'.encode())
		thread = threading.Thread(target = handle_client, args=(client,))
		thread.start()

if __name__ == '__main__':
	recieve()