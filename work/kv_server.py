import argparse
import socket
import threading
import requests
#import os
parser=argparse.ArgumentParser()
parser.add_argument('--host',default='127.0.0.1')
parser.add_argument ('--port',type=int,default=5678)
args=parser.parse_args()
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((args.host, args.port))
s.listen(5)

print('Waiting for connection...')
dic={}#Dictionary
storage=[]
#check=-1
with open('f://work/userpassword.txt','r') as file:
	getword=file.read()
file.close()
wordsp=getword.split()
aa=2
bb=0
user=[]
password=[]
try:
	while True:
		if aa%2==0:
			user.append(wordsp[bb])
			aa+=1
			bb+=1
		else:
			password.append(wordsp[bb])
			aa+=1
			bb+=1
except:
	pass
print(user,password)
def tcplink(sock,addr):
	print('Accept new connection from %s:%s...'%addr)
	sock.send(b'Welcome to use this server!')
	data=sock.recv(1024)
	while True:
		#time.sleep(1)
		if data.decode('utf-8')=='EXIT':
			break
		else:
			onedata=data.decode('utf-8')
			using=onedata.split()
			#time.sleep(1)
			if using[0]=='SET':
				dic[using[1]]=using[2]
				storage.append(using[1])
				sock.send(b'Success!')
			elif using[0]=='GET':
				if using[1] in storage:
					sock.send(dic[using[1]].encode('utf-8'))
				else:
					sock.send(b'404 Not Found')
			elif using[0]=='URL':
				if using[1] in storage:
					sock.send(dic[using[1]].encode('utf-8'))
				else:
					pass
					r=requests.get(using[2])
					with open('f://work/bb','wb') as f:
						f.write(r.content)
					f.close
					count=0
					with open('f://work/bb','rb') as f:
						q=f.read()
					f.close()
					for save in q:
						count+=1
					using[2]=str(count)
					dic[using[1]]=using[2]
					storage.append(using[1])
					sock.send(str(count).encode('utf-8'))
			elif using[0]=='AUTH':
				if using[1] in user:
					cc=user.index(using[1])
					if using[2]==password[cc]:
						sock.send(b'0')
					else:
						sock.send(b'-1')
				else:
					sock.send(b'1')
				'''
				try:
					cc=0
					cc=user.index(using[1])
					if using[2]==password[cc]:
						sock.send(b'0')
						#check=0
					else:
						sock.send(b'-1')
				except:
					sock.send(b'Unknown User!')
				'''
		data=sock.recv(1024)
	sock.close()
	print('Connection from %s:%sclosed.'%addr)
while True:
	sock,addr=s.accept()
	t=threading.Thread(target=tcplink, args=(sock,addr))
	t.start()
