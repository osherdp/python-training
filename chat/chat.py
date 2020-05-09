"""Run the chat against another endpoint.

Usage:
    chat.py <local-port> <remote-host> <remote-port> [--username <name>]
    chat.py (-h | --help)

Options:
    -u <name>, --username <name>    The user nickname [default: guest].
    -h, --help
"""
import select
import socket
import sys
import threading

from docopt import docopt


class Peer:
    def __init__(self, username: str, local_port: int):
        self.username = username

        self.server_socket = socket.socket()
        self.server_socket.bind((socket.gethostname(), local_port))
        self.server_socket.listen(3)

        self.client_socket = socket.socket()

    def start(self, remote_address: tuple):
        while True:
            readable, writable, error_sockets = select.select(
                [self.server_socket], [], [])

            for sock in readable:
                if sock is self.server_socket:
                    # new connection
                    connection, client_address = sock.accept()
                    connection.setblocking(False)

                else:
                    # existing connection
                    data = sock.recv(1024)  # CHANGE

                    if not data:
                        sock.close()

                    else:
                        print(data)     # CHANGE

            for sock in writable:
                if sock is self.client_socket:
                    # new connection
                    sock.connect(remote_address)




def main(local_port, remote_host, remote_port, username):
    pass


if __name__ == '__main__':
    arguments = docopt(__doc__)
    main(int(arguments["<local-port>"]), arguments["<remote-host>"],
         int(arguments["<remote-port>"]), arguments["--username"])
