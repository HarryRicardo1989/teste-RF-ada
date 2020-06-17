import requests
import json
from time import sleep

class RequestTx:
    def __init__(self):
        self.url_tx = 'http://10.8.0.126/atualiza/freq'
        pass
    def post_freq(self, freq, status):
        json_to_tx = {"STATUS":f'{status}',"FREQ":f'{freq}'}
        return requests.post(self.url_tx, json=json_to_tx).text
