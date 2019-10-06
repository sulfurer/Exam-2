import argparse
import socket
import threading
parser=argparse.ArgumentParser()
parser.add_argument('--host',default='127.0.0.1')
parser.add_argument ('--port',type=int,default=5678)
args=parser.parse_args()
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((args.host, args.port))
s.listen(5)

print('Waiting for connection...')
dic={}
storage=[]
def tcplink(sock,addr):
	print('Accept new connection from %s:%s...'%addr)
	sock.send(b'Welcome to use this server!')
	data=sock.recv(1024)
	while True:
		#time.sleep(1)
		if data.decode('utf-8')=='exit':
			break
		else:
			onedata=data.decode('utf-8')
			using=onedata.split()
			#time.sleep(1)
			if using[0]=='set':
				dic[using[1]]=using[2]
				storage.append(using[1])
				sock.send(b'Success!')
			else:
				if using[1] in storage:
					sock.send(dic[using[1]].encode('utf-8'))
				else:
					sock.send(b'404 Not Found')
		data=sock.recv(1024)
	sock.close()
	print('Connection from %s:%sclosed.'%addr)
while True:
	sock,addr=s.accept()
	t=threading.Thread(target=tcplink, args=(sock,addr))
	t.start()
