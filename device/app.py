# Importa as funcoes de controle de hardware e de requests HTTP
from lib_blink import estado_verde, estado_amarelo, estado_vermelho
from lib_blink import estado_completo, estado_desligado
from time import sleep
import requests


# De qual URL o estado sera obtido?
url_estado = "http://url.com"


def obtem_estado():
    r = requests.get('url_estado')
    return(r.text)
