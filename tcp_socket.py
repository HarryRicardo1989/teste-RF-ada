import socket
import address_commands as ac


class TcpSocket:
    def __init__(self):
        self.bufferSize = 1024

    def connect(self, data, addr, port):
        tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_client.connect((addr, port))
        tcp_client.send(data.encode())
        data = tcp_client.recv(self.bufferSize).decode()
        tcp_client.close()
        return data
