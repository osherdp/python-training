import sys
import msvcrt
import socket
import select


def user_non_blocking_input():
    collected = str(msvcrt.getche(), encoding="ASCII")

    while collected[-1] != b"\n":
        if msvcrt.kbhit():
            collected += str(msvcrt.getche(), encoding="ASCII")

    return collected


if __name__ == '__main__':
    try:
        server = socket.socket()
        server.setblocking(False)

        server.bind(("0.0.0.0", 1234))
        server.listen(3)

        inputs = [server, sys.stdin]
        outputs = []

        while inputs:
            readable, writable, exceptional = select.select(
                inputs, outputs, inputs, 1)

            for sock in readable:
                if sock is server:
                    connection, client_address = server.accept()
                    inputs.append(connection)

                    connection.send(sys.stdin.readline().encode())

                    print("Server after send.")

                else:
                    data = sock.recv(1024)
                    if data:
                        print(f"Other: {data.decode()}")

                        if sock not in outputs:
                            outputs.append(sock)

                    else:
                        if sock in outputs:
                            outputs.remove(sock)

                        inputs.remove(sock)
                        sock.close()

            for sock in writable:
                sock.send(sys.stdin.readline().encode())

    except OSError:
        client = socket.socket()
        client.connect(("127.0.0.1", 1234))

        while True:
            data = client.recv(1024)
            print(f"Other: {data.decode()}")

            send_msg = sys.stdin.readline()
            if send_msg.lower() == 'exit' or data == "":
                break

            else:
                client.sendto(send_msg.encode(), ("127.0.0.1", 1234))

        client.close()
