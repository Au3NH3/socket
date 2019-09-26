#!/usr/bin/python3
import socket

HOST=''
PORT=8000
host=(HOST,PORT)
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
	s.bind(host)
	s.listen(5)
	print('bind on: %s:%s' %(HOST,PORT))
	print('waiting for connection')
	
	while True:
		conn,addr=s.accept()
		
		with conn:
			print('Connected by: ', addr)
			# rec=b''
			# while True:
				# data=conn.recv(1024)
				# if not data:  break
				# rec+=data
			while True:
				rec=conn.recv(1024)
				conn.sendall(rec)
				print(rec.decode())
				if not rec:  break
			
print('connection closed')