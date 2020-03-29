from threading import Thread
import socket


# Multi-threaded server: TCP server socket Thread pool.
class ClientThread(Thread):
    client_lst = []
    address_lst = []

    def __init__(self, conn, ip, port):
        """
        Set the client's attributes, and adding to the client's list and addreess list.
        :param conn: The connection, represent each Client.
        :param ip: ip used, (the first value of address)
        :param port: Port used, (the second value of address)
        """
        Thread.__init__(self)
        self._conn = conn
        self._ip = ip
        self._port = port
        ClientThread.client_lst.append(conn)
        ClientThread.address_lst.append((ip, port))
        print("New server socket thread started for %s : %d\n" % (ip, port))

    def run(self):
        """
        A function that run automatically when initializing a thread.
        The func runs a loop that receives a massage from the clients and sends it to the other clients,
        according to the client_lst.
        If the massage is "exit" the func removes the client and ends the loop.
        """
        end_connection = False
        while not end_connection:

            data = self._conn.recv(1024).decode("utf-8")
            if data == "exit":
                self.remove_client()
                end_connection = True

            else:
                print("Server received data from %s: %s\n" % (str((self._ip, self._port)), data))  # Print to server

                # If there are no other clients.
                if len(ClientThread.client_lst) == 1:
                    self._conn.send(bytes("There are no other clients in this chat", "utf-8"))

                else:
                    # Sends the massage to the other clients.
                    for conn in ClientThread.client_lst:
                        if conn != self._conn:
                            conn.send(bytes(f"From {self._port}: " + data, "utf-8"))

    def remove_client(self):
        """
        When called, the func closes the connection and removes from the clients list and address list.
        """
        self._conn.close()
        ClientThread.address_lst.remove((self._ip, self._port))
        ClientThread.client_lst.remove(self._conn)


# Multi-threaded Python server : TCP Server Socket Program
def main():
    # Set server parameters.
    tcp_ip = '0.0.0.0'
    tcp_port = 2004

    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tcp_server.bind((tcp_ip, tcp_port))
    tcp_server.listen(5)

    # An infinite loop that waiting for clients to connect to the server.
    # A new thread is created For every connection and a new argument of ClientThread class.
    while True:

        print("Multi-threaded Python server : Waiting for connections from TCP clients...")
        (conn, (ip, port)) = tcp_server.accept()
        new_thread = ClientThread(conn, ip, port)
        new_thread.start()


if __name__ == '__main__':
    main()
