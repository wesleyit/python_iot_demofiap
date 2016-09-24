# Importa as funcoes de controle de hardware e de requests HTTP
from lib_blink import estado_verde, estado_amarelo, estado_vermelho
from lib_blink import estado_campainha, estado_completo, estado_desligado
from iron_cache import IronCache
from time import sleep


def obtem_estado():
    cache = IronCache(project_id="57e7006d1e0aa6000858dc32",
                      token="Dcc5Bq9UWP1qtQuERZXF")
    cache.name = 'IoT_Demo'
    try:
        item = cache.get(key="estado")
    except:
        item = None
        return item.value


def loop_principal():
    estado = obtem_estado()
    eval(estado)()


while True:
    loop_principal
    sleep(5)
