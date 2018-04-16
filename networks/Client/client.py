import socket
import os
import sys
import pygame

HOST = 'localhost'    
PORT = 909
BUFFER =1024

queue = []

def python_client():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    pygame.init()
    pygame.mixer.init()

    while (1):
        msg = input("<YOU>: ")
        s.send(msg.encode('utf-8'))
        rec_msg = s.recv(BUFFER)
        rec_msg = rec_msg.decode('utf-8')
        print("<" + HOST +">: " + rec_msg)
        if (rec_msg == "What File?"):
            file(s)
        print(queue)
        if (rec_msg == "PLAY SONG"):
            pygame.mixer.music.load (queue.pop() )
            pygame.mixer.music.play()
            s.send("Music is Playing".encode())
            recv= s.recv(BUFFER)
            recv = recv.decode('utf-8')
            print("<" + HOST +">: " + rec_msg)
        if (rec_msg == "PAUSE SONG"):
            pygame.mixer.music.pause()
            s.send("Music Paused".encode())
            recv= s.recv(BUFFER)
            recv = recv.decode('utf-8')
            print("<" + HOST +">: " + rec_msg)
        if (rec_msg == "RESUME SONG"):
            pygame.mixer.music.unpause()
            s.send("Music Resumed".encode())
            recv= s.recv(BUFFER)
            recv = recv.decode('utf-8')
            print("<" + HOST +">: " + rec_msg)
        if (rec_msg == "NEXT SONG"):
            if(queue != []):
                pygame.mixer.music.load (queue.pop() )
                pygame.mixer.music.play()
                s.send("Next Song Playing".encode())
                recv= s.recv(BUFFER)
                recv = recv.decode('utf-8')
                print("<" + HOST +">: " + rec_msg)
            else:
                s.send("Playlist is Empty. Load More Songs".encode())
                recv= s.recv(BUFFER)
                recv = recv.decode('utf-8')
                print("<" + HOST +">: " + rec_msg)
def file(s):
    name = input("<YOU>: ")
    print(name)
    s.send(name.encode('utf-8'))
    with open('new_' +name, 'wb') as f:
        print("ALERT...writing to file..")
        while True:
            data = s.recv(BUFFER)
            #data = data.decode('utf-8')
            #print(data)
            if (data[-3:] == "END".encode('utf-8')):
                print("ALERT...finished writing to file..")
                queue.append('new_'+name)
                #s.send(str(queue).encode())
                break
            if not data:
                break
            f.write(data)
        f.close()
    return


if __name__ == "__main__":
    sys.exit(python_client())