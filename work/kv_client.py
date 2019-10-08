import socket
import threading
import argparse
import time
check=-1
while True:
	try:
		parser=argparse.ArgumentParser()
		parser.add_argument('--host',default='127.0.0.1')
		parser.add_argument('--port',type=int,default=5678)
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
		print("Please enter command(Press 'EXIT' to sign out):")
		data=input()
		'''
		def com(n):
			onedata=n.encode('utf-8')
			s.send(onedata)
			print(s.recv(1024).decode('utf-8'))
			print("Please enter command(Press 'EXIT' to sign out):")
			n=input()
		'''
		while data!='EXIT':
			using=data.split()
			if data=='':
				print("No Command!\nPlease enter the command:")
				data=input()
			elif using[0]=='SET' or using[0]=='GET':
				if using[0]=='SET':
					if len(using)==3:
						#'''
						onedata=data.encode('utf-8')
						s.send(onedata)
						print(s.recv(1024).decode('utf-8'))
						print("Please enter command(Press 'EXIT' to sign out):")
						data=input()
						#'''
						#com(data)
					else:
						print("Command using error!\nExample: SET (KEY) (VALUE)")
						data=input()
						continue
				else:
					if len(using)==2:
						onedata=data.encode('utf-8')
						s.send(onedata)
						print(s.recv(1024).decode('utf-8'))
						print("Please enter command(Press 'EXIT' to sign out):")
						data=input()
					else:
						print("Command usage error!\nExample: GET (KEY)")
						data=input()
						continue
			#elif data=='EXIT':
			#	s.send(b'EXIT')
			#	s.close()
			elif using[0]=='URL':
				#pass
				if check==0:
					if len(using)==3:
						onedata=data.encode('utf-8')
						s.send(onedata)
						print(s.recv(1024).decode('utf-8'))
						print("Please enter command(Press 'EXIT' to sign out):")
						#data=input()
					else:
						print("Command usage error!\nExample: URL (key) (url)")
						#data=input()
				else:
					print("You can only use this program after login in!\nCommand:AUTH (user) (password)")
					#data=input()
				data=input()
			elif using[0]=='AUTH':
				if len(using)==3:
					onedata=data.encode('utf-8')
					s.send(onedata)
					out=s.recv(1024).decode('utf-8')
					if out=='0':
						print("Login in!\nReturn 0")
						check=0
					elif out=='1':
						print("Unkonwn User!")
					else:
						#pass
						print("The user or the password is wrong!")
				else:
					print("Command usage error!\nExample: AUTH (user) (password)")
				data=input()
			else:
				print("Unkonwn Command!")
				print("Please enter again:")
				data=input()
		s.send(b'EXIT')
		s.close()
		break
