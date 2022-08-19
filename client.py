import socket

server_ip = socket.gethostname()
server_port = 56300
srv_connection = server_ip, server_port


def clt():
    client_skt = socket.socket()
    client_skt.connect(srv_connection)
    client_skt.send('YO!'.encode())
    client_skt.close()

    # print(f"We got connection from {addrs}")
    # while True:
    #     data = conn.recv(2052).decode()
    #     if not data:
    #         break
    #     print(f"Received message: {data}")
    #     msg = input(">>> ")
    #     if msg == "stop":
    #         break
    #     conn.send(msg.encode())
    # conn.close()


if __name__ == '__main__':
    clt()
