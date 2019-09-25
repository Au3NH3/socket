#!/usr/bin/python3
import socket
# HOST = '202.38.64.59'
PORT=80
HOST=input('input host: ')
msg='GET / HTTP/1.1\r\nHost:'
rec=b''
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((HOST, PORT))
	print('连接到%s:%s成功\n' %(HOST,PORT))
	msg=msg+HOST+'\r\n\r\n'
	print(msg)
	s.sendall(msg.encode())
	n=0
	while True:
		data = s.recv(1024)
		if not data: break
		rec+=data
		n+=1
	try:
		print(rec.decode())
	except:
		print(rec.decode('gb2312'))
	print('recive %s times' %n)
	