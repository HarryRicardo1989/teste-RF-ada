import os


class RequestCommands:
    def __init__(self):
        pass

    def comand(self, comando):
        retorno = os.popen(comando)
        return retorno.read().strip().strip('\n').strip()
