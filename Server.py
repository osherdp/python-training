from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

CLIENTS = {}
IP = '127.0.0.1'
PORT = 8820
SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind((IP, PORT))


def accept_new_connections():
    while True:
        client, client_address = SERVER.accept()
        msg = 'type your username:'
        client.send(msg.encode())
        Thread(target=handle_client, args=(client,)).start()


def handle_client(client):
    name = client.recv(1024).decode()
    msg = 'to leave, type "quit"'
    client.send(msg.encode())
    message = name + ' has joined the chat!'
    broadcast(message.encode(), client)
    CLIENTS[client] = name
    while True:
        msg = client.recv(1024)
        if msg.decode() != 'quit':
            broadcast(msg, client, name + ": ")
        else:
            msg = name + ' has left the chat.'
            client.close()
            del CLIENTS[client]
            broadcast(msg.encode(), client)
            break


def broadcast(msg, client, start=""):
    for sock in CLIENTS:
        if sock != client:
            sock.send(start.encode() + msg)


if __name__ == "__main__":
    SERVER.listen(5)
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=accept_new_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()
