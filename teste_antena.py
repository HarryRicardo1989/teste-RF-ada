#!/bin/python3

import address_commands as ac
from tcp_socket import TcpSocket
from ada_control import AdaControl
from gqrx_control import RemoteControl
from time import sleep


class TesteAda:
    def __init__(self):
        self.gqrx_ctr = RemoteControl(*ac.gqrx_addr_port)
        self.ada_ctr = AdaControl()
        self.signal_power = 0.0
        pass

    def ada_teste(self, pos_az_init, pos_az_end, pos_el, media_num):

        for pos_az in range(int(pos_az_init), int(pos_az_end)+1, 1):
            position = False
            print(pos_az)
            self.ada_ctr.set_ada_pos(float(pos_az), pos_el)
            while not position:
                position = bool(self.compare_position(
                    pos_az, pos_el, self.ada_ctr.get_ada_pos()))
                sleep(0.1)
                print(position)

            self.grava_resultado(pos_az, self.gqrx(media_num))
        print('finalizado')

    def compare_position(self, os_az_setted, pos_el_setted, pos_getted):
        return float(pos_getted[0]) == float(os_az_setted) and float(pos_getted[1]) == float(pos_el_setted)

    def gqrx(self, media_num):
        self.gqrx_ctr.set_controls(ac.set_freq, ac.NOAA19)
        signal_list = []
        for teste in range(0, media_num):
            signal_power = float(self.gqrx_ctr.get_status(ac.signal_power))
            signal_list.append(signal_power)
            print(f'{teste+1} Signal Power {signal_power} dBFS')
            sleep(0.5)
        return sum(signal_list) / len(signal_list)

    def grava_resultado(self, pos, signal_power):
        with open('/tmp/teste-ADA.csv', 'a') as file:
            file.write(f'{pos},{signal_power} \n')


if __name__ == '__main__':

    az_inicial = float(input('Informe o Azimute Inicial :'))
    az_final = float(input('Informe o Azimute Final :'))
    elevacao = float(input('Informe a Elevaçao do teste :'))
    numero_amostras = int(input(
        'Informe o numero de amostras para a media de recepcao :'))

    TesteAda().ada_teste(az_inicial, az_final, elevacao, numero_amostras)
