#!/usr/bin/python3
import socket
# host = '202.38.64.59'
port=8000
host=input('input host: ')
# host=socket.gethostname()
if ' ' in host:
	host,port=host.split(' ')


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((host,port))
	print('连接到%s:%s成功\n' %(host,port))

	while True:
		msg=input('>>')
		if msg=='q':  break
		s.sendall(msg.encode())
		# n=0
		rec=b''
		# while True:
			# data = s.recv(1024)
			# if not data: break
			# rec+=data
			# n+=1
		rec=s.recv(1024)
		try:
			print(rec.decode())
		except:
			print(rec.decode('gb2312'))
		# print('recive %s times' %n)
	