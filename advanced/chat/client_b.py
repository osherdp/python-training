# Python TCP Client B
import socket
from threading import Thread


def write(tcp_client_b):
    """
    This func runs a loop that waits for a text from the client and send it to the server.
    When "exit" is entered, the loop stops.
    :param tcp_client_b: The client.
    :return:
    """
    exit_flag = False
    msg = input("tcpClientB: Enter message/ Enter exit:\n")
    while not exit_flag:
        if msg == "exit":
            exit_flag = True
        tcp_client_b.send(bytes(msg, "utf-8"))
        msg = input("")


def read(tcp_client_b, buffer_size):
    """
    The func receives data from the server and prints it.
    :param tcp_client_b: The client.
    :param buffer_size: The size of the buffer of the data that received.
    """
    while True:
        data = tcp_client_b.recv(buffer_size).decode("utf-8")
        print(data)


def main():
    """
    Sets the parameters of the client, and starts the write() and read() functions in 2 threads.
    """
    # If working in different computers the host name should be the same as the server host name.
    host = socket.gethostname()
    port = 2004
    buffer_size = 2000

    tcp_client_b = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_client_b.connect((host, port))

    # Write thread.
    w_thread = Thread(target=write, args=(tcp_client_b,))

    # Read thread.
    r_thread = Thread(target=read, args=(tcp_client_b, buffer_size))

    w_thread.start()
    r_thread.start()


if __name__ == '__main__':
    main()
