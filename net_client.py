
import socket

def main():
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	addr = ("localhost", 25252)
	sock.connect(addr)
	
	for i in range(1, 11):
		msg = "h" * i
		sock.sendall(msg.encode())
		newMsg = sock.recv(1024).decode()
		print(newMsg)

main()
