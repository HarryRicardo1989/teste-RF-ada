'''
Config File for address, port and data-send to use in socket
'''

'''
Address and ports for ADA-Server
'''
#port_gqrx = input("digite a porta do GQRX")

predict_addr_port = ('127.0.0.1', 1210)
gqrx_addr_port = ('127.0.0.1', 1212)

'''
Predict Commands
'''
sat_list = 'GET_LIST'
doppler = 'GET_DOPPLER'
sat_pos = 'GET_SAT_POS'
predictions = 'PREDICT'

'''
schedules
'''
number_of_pass = 3
sat_scheduled = (3, 4, 5)

# _____________________________________
'''
gqrx commands


'''
# _____________________________________
# get commands

signal_power = 'l STRENGTH'
get_mode = 'm '
# get_mode = 'm ' (OFF, RAW, AM, FM, WFM, WFM_ST, WFM_ST_OIRT, LSB, USB, CW, CWL, CWU)
get_freq = 'f '
get_record_status = 'u '
get_vfo = 'v '
# _____________________________________
# set commands

set_mode = 'M '
set_freq = 'F '
set_record_status = 'U '
set_vfo = 'V '
aos_record = 'AOS'
los_record = 'LOS'


'''
satellites Frequency
'''

NOAA19 = '137.1e6'
