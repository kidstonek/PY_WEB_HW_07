import socket

server_ip = socket.gethostname()
server_port = 56300


def srv():
    sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sck.bind((server_ip, server_port))
    sck.listen(2)
    conn, addrs = sck.accept()
    print(f"We got connection from {addrs}")
    while True:
        data = conn.recv(2052).decode()
        if not data:
            break
        print(f"Received message: {data}")
        msg = input(">>> ")
        if msg == "stop":
            break
        conn.send(msg.encode())
    conn.close()


def main():
    srv()


if __name__ == '__main__':
    main()


