import socket
SERVER_IP = '192.168.56.1'
SERVER_PORT= 6767
# print ("hello world")
# sockt shit here this is the server suppose to this is what we send to "hack the user i guess "

with socket.socket(socket.AF_INET,socket.SOCK_STREAM)as s :
    s.bind((SERVER_IP , SERVER_PORT))
    s.listen(1)
    conn,addr = s.accept()
    print ("should be working ")
    print (f"connection established from :{addr}")
    with conn:
        while True:
            conn.send(b'hello world ')
            break