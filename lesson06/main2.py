import socket


s = socket.socket()
s.connect(("localhost", 9090))
print("Connected")

while True:
    print('sending')
    s.send(b"World")



