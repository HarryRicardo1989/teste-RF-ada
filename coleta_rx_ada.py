

import address_commands as ac
from tcp_socket import TcpSocket
from ada_control import AdaControl
from gqrx_control import RemoteControl
from post_commands import RequestTx
from time import sleep


class ColetaRxADA:
    def __init__(self, **kwargs ):
        '''
            pos_el=float[degrees], exemple 0.15 max 2 decimal point
            pos_az_init=float[degrees], exemple 0.00 max 2 decimal point
            pos_az_end=float[degrees], exemple 359.21 max 4 decimal point
            freq_init=float[MHZ], exemple 137.1234 max 4 decimal point
            freq_end=float[MHZ], exemple 147.1234 max 4 decimal point
            pos_step=float[degrees], exemple 0.15 max 2 decimal point
            freq_div=int, 
            media_num=int
        '''
        # atributos diversos
        self.__pos_mult = 100
        self.__freq_mult = 1000000
        self.__media_num = int(kwargs['media_num'])
        self.__signal_power = 0.0
        self.__nome_teste = kwargs['nome_teste']

        # atributos posiçao
        self.__pos_el = int(kwargs['pos_el']*self.__pos_mult)
        self.__pos_az_init = int(kwargs['pos_az_init']*self.__pos_mult)
        self.__pos_az_end = int(kwargs['pos_az_end']*self.__pos_mult)
        self.__pos_step = int(kwargs['pos_step']*self.__pos_mult)

        # atributos frequencia
        self.__freq_init = int(kwargs['freq_init']*self.__freq_mult)
        self.__freq_end = int(kwargs['freq_end']*self.__freq_mult)
        self.__freq_div = int(kwargs['freq_div'])
        self.__freq_list = self.__freqs_num()

        

        # instancias ...
        self.__gqrx_ctr = RemoteControl(*ac.gqrx_addr_port)
        self.__ada_ctr = AdaControl()
        self.__tx_send = RequestTx()

    def run_teste(self): 
        pos_atual = self.__pos_az_init
        while pos_atual <= self.__pos_az_end:
            print(pos_atual/self.__pos_mult)
            self.__ada_ctr.set_ada_pos((pos_atual/self.__pos_mult), (self.__pos_el/self.__pos_mult))
            position = False
            print('Wait positioning.')
            while not position:
                position = bool(self.__compare_position((pos_atual/self.__pos_mult), self.__pos_el/self.__pos_mult, self.__ada_ctr.get_ada_pos()))
                sleep(0.1)
                print(f'Em posicao: {position}')
            self.__gqrx(pos_atual)
            pos_atual += self.__pos_step
        self.__tx_send.post_freq(0.0,'OFF')
        self.__ada_ctr.set_ada_pos(0.0,-1.0)

        print('Teste Finalizado')

    def __compare_position(self, pos_atual, pos_el, pos_rcv):   
        return float(pos_rcv[0]) == float(pos_atual) and float(pos_rcv[1]) == float(pos_el)

    def __gqrx(self, pos_atual):
        for frequencia in self.__freq_list: 
            print(frequencia)
            answer_tx= self.__tx_send.post_freq(frequencia,'ON')
            print(f'Transmissor ajustado: {(answer_tx == str(frequencia))}')
            while not answer_tx == str(frequencia):
                pass
            self.__gqrx_ctr.set_controls(ac.set_freq, frequencia)
            sleep(1)
            signal_list = []
            for teste in range(0, self.__media_num):
                signal_power = float(self.__gqrx_ctr.get_status(ac.signal_power))
                signal_list.append(signal_power)
                print(f'{teste+1} Signal Power {signal_power} dBFS')
                sleep(0.5)
            media_coleta = sum(signal_list) / len(signal_list)
            self.__grava_resultado(pos_atual/self.__pos_mult, frequencia, media_coleta)
        return True


    def __grava_resultado(self, pos, freq, signal_power):
        with open(f'/tmp/teste-ADA-{self.__nome_teste}.csv', 'a') as file:
            file.write(f'{pos};{freq};{signal_power} \n')

    def __freqs_num(self):
        freq_atual = self.__freq_init
        freq_list=[freq_atual/self.__freq_mult,]
        freq_step = (self.__freq_end - self.__freq_init)/self.__freq_div
        for item in range(0, self.__freq_div):
            freq_atual += freq_step 
            freq_list.append(round(freq_atual/self.__freq_mult,6))
        return freq_list
