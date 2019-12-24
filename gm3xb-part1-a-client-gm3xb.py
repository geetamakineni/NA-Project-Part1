import socket
host = 'localhost'
port = 1024

def connect(host,port):
	serv=socket.socket()
	serv.connect((host,port))
	return serv

def exchange_messages(m,serv):
	while True:
		if m == "Bye from Client Geetanjali":
			serv.send(str.encode(m))
			message=str(serv.recv(1024).decode())
			print(message)
			if(message == "Bye from Server Geetanjali"):
				break
			else:
				m=input('Enter another message... ')

		elif m == "Hello from Client Geetanjali":
			serv.send(str.encode(m))
			message=str(serv.recv(1024).decode())
			print(message)
			m=input("Enter another message... ")
		else:
			serv.send(str.encode(m))
			message=str(serv.recv(1024).decode())
			print(message)
			m=input("Enter standard messages...")

def main():
	serv=connect(host,port)
	m=input("Enter message here...")
	exchange_messages(m,serv)
	serv.close()

if __name__== "__main__":
	main()
