import socket
host = ''
port = 1024

def bind(host,port):
	serv=socket.socket()
	serv.bind((host, port))
	print('Messages are below')
	serv.listen(1)
	conn,addr = serv.accept()
	return conn

def exchange_messages(conn):
	while True:
		message=str(conn.recv(1024).decode())
		if message == "Bye from Client Geetanjali":
			print(message)
			conn.send(str.encode("Bye from Server Geetanjali"))
			break
		elif message == "Hello from Client Geetanjali":
			print(message)
			conn.send(str.encode("Hello from Server Geetanjali"))
		else:
			print(message)
			conn.send(str.encode(message))
	
def main():
	conn=bind(host, port)
	exchange_messages(conn)
	conn.close()

if __name__== "__main__":
	main()
