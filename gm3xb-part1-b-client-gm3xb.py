import socket
host = 'localhost'
port = 1023
def connect(host,port):
	serv=socket.socket()
	serv.connect((host, port))
	return serv
def transfer_data(fname,serv):
	while True:
		if fname == "exit":
			serv.send(str.encode(fname))
			data=str(serv.recv(1024).decode())
			print(data)
			break
		else :  
			f = open(fname,'rb')
			l = f.read(1024)
			print("data sending ", end =" ")
			while (l):
				print(".", end =" ")
				serv.send(l)
				l = f.read(1024)
			f.close()
			serv.send(str.encode("File transfer complete"))
			print("\n")

			while True:
				data = serv.recv(1024)
				if str(data).find("File sent back from server") != -1:
					break
				print(data)
			print("File received back\n")
			fname= input("Enter another file name or type exit : ")
def main():
	serv=connect(host, port)
	fname=input('Enter file name here or type exit : ')
	transfer_data(fname,serv)
	serv.close()

if __name__== "__main__":
    main()
