import socket

port = 8080
print("hostname : " + str(socket.gethostbyname(socket.gethostname())))

s = socket.socket()
print("Socket successfuly created")

s.bind(("", port))

s.listen(5)
print("Socket is listenning")

while True:
    c, addr = s.accept()
    print("Got connection from : " + str(addr))

    c.send(b'test')

    c.close()
