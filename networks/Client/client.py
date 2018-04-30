import socket
import os
import sys
import pygame

HOST = 'localhost'    
PORT = 9006
BUFFER = 1024

queue = []


def python_client():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv = False
    s.connect((HOST, PORT))
    pygame.init()
    pygame.mixer.init()
    curr_song = ""
    
    while 1:
        if serv is False:
            msg = input("<YOU>: ")
            s.send(msg.encode('utf-8'))

        rec_msg = s.recv(BUFFER)
        rec_msg = rec_msg.decode('utf-8')
        print("<" + HOST + ">: " + rec_msg)
        if rec_msg == "What File?":
            file(s)
            s.send(str(queue).encode())
            rec_msg = s.recv(BUFFER)
            rec_msg = rec_msg.decode('utf-8')
            print("<" + HOST + ">: " + rec_msg)
        if rec_msg == "PLAY SONG":
            serv = True
            curr_song = queue.pop()
            pygame.mixer.music.load(curr_song)
            pygame.mixer.music.play()     
            # s.send((curr_song+ " is playing").encode());
        if rec_msg == "PAUSE SONG":
            pygame.mixer.music.pause()
            serv = True
            # s.send("Music Paused".encode())
        if rec_msg == "RESUME SONG":
            serv = True
            pygame.mixer.music.unpause()
            s.send("Music Resumed".encode())
        if rec_msg == "NEXT SONG":
            # serv = True
            if queue != []:
                curr_song = queue.pop()
                pygame.mixer.music.load (curr_song)
                pygame.mixer.music.play()
                # s.send((curr_song + " is now playing").encode())
            else:
                s.send("Playlist is Empty. Load More Songs".encode())
                serv = True
        if rec_msg == "REWIND SONG":
            pygame.mixer.music.rewind()
            serv = True
        if rec_msg == "INCREASE VOLUME":
            vol = pygame.mixer.music.get_volume()
            if vol < 1:
                vol = vol + 0.1
            pygame.mixer.music.set_volume(vol)
            serv = True
        if rec_msg == "DECREASE VOLUME":
            vol = pygame.mixer.music.get_volume()
            if vol > 0:
                vol = vol - 0.1
            pygame.mixer.music.set_volume(vol)
            serv = True
        else:
            serv = False


def file(s):
    name = input("<YOU>: ")
    s.send(name.encode('utf-8'))
    try:
        with open('new_' + name, 'wb') as f:
            print("ALERT...writing to file..")
            while True:
                data = s.recv(BUFFER)
                if data[-3:] == "END".encode('utf-8'):
                    print("ALERT...finished writing to file..")
                    queue.append('new_'+name)
                    break
                if not data:
                    break
                f.write(data)
            f.close()
    except EnvironmentError as e:
        print("Error: " + e)
    return


if __name__ == "__main__":
    sys.exit(python_client())
