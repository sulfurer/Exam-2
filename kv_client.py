import socket
import threading
import argparse
import time
while True:
	try:
		parser=argparse.ArgumentParser()
		parser.add_argument('--host',default='127.0.0.1')
		parser.add_argument ('--port',type=int,default=5678)
		args=parser.parse_args()
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.connect((args.host, args.port))
	except:
		print("ConnectionRefusedError!")
		print("Reconnect after 5 second...")
		time.sleep(5)
	else:
		print(s.recv(1024).decode('utf-8'))
		data=''
		print("Please enter command(Press 'exit' to sign out):")
		data=input()
		'''
		def com(n):
			onedata=n.encode('utf-8')
			s.send(onedata)
			print(s.recv(1024).decode('utf-8'))
			print("Please enter command(Press 'exit' to sign out):")
			n=input()
		'''
		while data!='exit':
			using=data.split()
			if data=='':
				print("No Command!\nPlease enter the command:")
				data=input()
			elif using[0]=='set' or using[0]=='get':
				if using[0]=='set':
					if len(using)==3:
						#'''
						onedata=data.encode('utf-8')
						s.send(onedata)
						print(s.recv(1024).decode('utf-8'))
						print("Please enter command(Press 'exit' to sign out):")
						data=input()
						#'''
						#com(data)
					else:
						print("Command using error!\nExample:set (key) (value)")
						data=input()
						continue
				else:
					if len(using)==2:
						onedata=data.encode('utf-8')
						s.send(onedata)
						print(s.recv(1024).decode('utf-8'))
						print("Please enter command(Press 'exit' to sign out):")
						data=input()
					else:
						print("Command using error!\nExample get (key)")
						data=input()
						continue
			#elif data=='exit':
			#	s.send(b'exit')
			#	s.close()
			else:
				print("Unkonwn Command!")
				print("Please enter again:")
				data=input()
		s.send(b'exit')
		s.close()
		break
