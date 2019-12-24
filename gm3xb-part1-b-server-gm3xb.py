import socket
host = ''
port = 1023
def bind(host,port):
	serv=socket.socket()
	serv.bind((host, port))
	print('messages ...')
	serv.listen(1)
	conn,addr = serv.accept()
	return conn
def transfer_data(conn):
	while True:
		data=conn.recv(1024)
		if str(data.decode()) == "exit":
			conn.send(str.encode("server gone"))
			print(str(data.decode()))
			break		
		else:
			with open('output.txt', 'wb') as fp:
				while True:
					print(data)
					fp.write(data)
					if str(data).find("File transfer complete") != -1:
						fp.write(str.encode("\n This line was added by me in the Server !!! \n"))
						print("\n This line was added by me in the Server !!! \n")
						break
					data = conn.recv(1024)

			fp = open('output.txt','rb')
			chunk = fp.read(1024)
			while (chunk):
				conn.send(chunk)
				chunk = fp.read(1024)
			fp.close()
			conn.send(str.encode("File sent back from server"))
def main():
	conn=bind(host, port)
	transfer_data(conn)
	conn.close()

if __name__== "__main__":
	main()
