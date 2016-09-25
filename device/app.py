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
        print("Item %s obtido via API") % item
        return item.value
    except:
        print("Impossivel obter o item.")
        return "estado_verde"


def loop_principal():
    print("Atualizando estado...")
    estado = obtem_estado()
    print("Estado = %s") % estado
    eval(estado)()


print("Iniciando loop principal")
iteracao = 1
while True:
    print("------------------------------------------------")
    print("Rodando a iteracao %d") % iteracao
    loop_principal()
    iteracao += 1
    sleep(5)
