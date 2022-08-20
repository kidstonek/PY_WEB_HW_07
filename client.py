import socket

server_ip = socket.gethostname()
server_port = 56300
srv_connection = server_ip, server_port


def clt():
    client_skt = socket.socket()
    client_skt.connect(srv_connection)
    client_skt.send(str(input('Type your first message: ')).encode())
    while True:
        data = client_skt.recv(2052).decode()
        if data:
            print(f'You received message {data}')
        if data == 'bye':
            print('Server closed connection by key word "bye"')
            break
        client_skt.send(str(input('Your message: ')).encode())
    client_skt.close()


if __name__ == '__main__':
    clt()
