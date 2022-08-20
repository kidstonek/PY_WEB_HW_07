import socket
import asyncio

server_ip = socket.gethostname()
server_port = 56300


def srv():
    print(f"Server started!!! on port {server_port}")
    sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sck.bind((server_ip, server_port))
    sck.listen(2)
    conn, addrs = sck.accept()
    print(f"We got connection from {addrs}")
    try:
        while True:
            data = conn.recv(2052).decode()
            if not data:
                break
            print(f"Received message: {data} from client {addrs[0]}")
            msg = input(">>> ")
            if msg == "stop":
                break
            conn.send(msg.encode())
    except KeyboardInterrupt:
        print('Connection stopped')
        conn.send('bye'.encode())
    finally:
        conn.close()


def main():
    srv()


if __name__ == '__main__':
    main()


