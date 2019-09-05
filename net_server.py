import socket

def main():
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	addr = ("0.0.0.0", 25252)
	sock.bind(addr)
	sock.listen(5)
	(connectedSock, clientAddress) = sock.accept()
	while(True):
		try:
			msg = connectedSock.recv(1024).decode()
		except ConnectionAbortedError:
			connectedSock.close()
			break
		message = "Here's the data: " + msg + " END"
		connectedSock.sendall(message.encode())


main()
