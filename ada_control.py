from request_commands import RequestCommands


class AdaControl:
    def __init__(self):
        self.comando = RequestCommands()
        pass

    def set_ada_pos(self, pos_az, pos_el):
        self.comando.comand(f'sudo ada pos -az {pos_az} -el {pos_el}')

    def get_ada_pos(self):
        position = self.comando.comand(
            'cat /opt/ada_server/temp/PosicaoInicial.txt | xargs').replace('@AZ', '').replace('EL', '').strip('#')
        return position.split()
