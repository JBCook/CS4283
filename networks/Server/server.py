import socket
import sys

HOST = 'localhost'
PORT = 9006
BUFFER = 1024

def python_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(10)
    conn= None
    while (1):
        if conn is None:
            conn, addr = s.accept()
        msg = conn.recv(BUFFER)
        msg = msg.decode('utf-8')
        print("<", s.getsockname(), ">: " , msg)
        if (msg == "File Request"):
            conn.send("What File?".encode('utf-8'))
            file(conn,s)
        else:
            msg = input("<YOU>: ")
            conn.send(msg.encode('utf-8'))

def file(c,s):
    filename = c.recv(BUFFER)
    filename = filename.decode('utf-8')
    print("<", s.getsockname(), ">: " , filename)
    with open(filename, 'rb') as f:
        for data in f:
            c.sendall(data)
        c.send("END".encode('utf-8'))
    
if __name__ == "__main__":
    sys.exit(python_server())