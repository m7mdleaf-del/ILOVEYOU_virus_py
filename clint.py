import socket

SERVER_IP = '192.168.56.1'
SERVER_PORT= 6767


with socket.socket(socket.AF_INET,socket.SOCK_STREAM)as s :
    s.connect((SERVER_IP,SERVER_PORT))
    data=s.recv(1024)
    print(data)

input()