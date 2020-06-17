from tcp_socket import TcpSocket


class RemoteControl:
    def __init__(self, *addr_port):
        self.addr_port = addr_port
        self.gqrx_control = TcpSocket()

    def set_controls(self, command, parameter, ):
        return self.gqrx_control.connect(f'{command} {parameter}e6', *self.addr_port)

    def get_status(self, command):
        return self.gqrx_control.connect(f'{command}', *self.addr_port)
