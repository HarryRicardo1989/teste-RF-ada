#!/usr/bin/python3
from coleta_rx_ada import ColetaRxADA
from time import sleep

if __name__ == '__main__':
    
    nome_teste = input('Digite o nome do teste: ')
    pos_el = float(input('Digite a posiçao de Elevaçao: '))
    pos_az_init = float(input('Digite o Azimute Inicial: '))
    pos_az_end = float(input('Digite o Azimute Final: ')) 
    freq_init = float(input('Digite a Frequencia Inicial: '))
    freq_end =float(input('Digite a Frequencia Final: '))
    freq_div = int(input('Digite a Quantidade de divisoes da faixa de frequencia: '))
    media_num = int(input('Digite a Quantidade de amostras por Frequencia: '))
    pos_step = 0.1
    if pos_az_init != pos_az_end:
        pos_step = float(input('Digite a taxa de Variacao de Azimute: '))
    else:
        print(f'Azimute fixo em: {pos_az_init} !')
    sleep(5)

    teste = ColetaRxADA(pos_step=pos_step, pos_el=pos_el, pos_az_init=pos_az_init, pos_az_end=pos_az_end, freq_init=freq_init,
                                freq_end=freq_end, freq_div=freq_div, media_num=media_num, nome_teste=nome_teste)
    teste.run_teste()
    print(f'O teste Foi salvo no arquivo /tmp/teste-ADA-{nome_teste}.csv')