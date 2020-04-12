from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

from pip._vendor.distlib.compat import raw_input


IP = '127.0.0.1'
PORT = 8820
CLIENT_SOCKET = socket(AF_INET, SOCK_STREAM)
CLIENT_SOCKET.connect((IP, PORT))


def recv():
    while True:
        try:
            msg = CLIENT_SOCKET.recv(1024).decode()
            print(msg)
        except:
            break


def send():
    msg = raw_input('')
    CLIENT_SOCKET.send(msg.encode())
    if msg.strip() == "quit":
        CLIENT_SOCKET.close()
        return False
    return True


if __name__ == "__main__":
    receive_thread = Thread(target=recv)
    receive_thread.start()
    done = True
    while done:
        done = send()
