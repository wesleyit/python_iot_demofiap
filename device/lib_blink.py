# Importando bibliotecas de GPIO do Orange PI
from pyA20.gpio import gpio
from pyA20.gpio import port
from time import sleep
gpio.init()


# Definindo as portas de cada componente e os estados padrao
porta_led_verde = port.PA7
porta_led_amarelo = port.PA8
porta_led_vermelho = port.PA9
porta_campainha = port.PA10
saida = gpio.OUTPUT
ligada = gpio.HIGH
desligada = gpio.LOW


# Configura as portas para saida de tensao
gpio.setcfg(porta_led_vermelho, saida)
gpio.setcfg(porta_led_amarelo, saida)
gpio.setcfg(porta_led_verde, saida)
gpio.setcfg(porta_campainha, saida)


# Metodo auxiliar para ligar uma porta
def ligar_porta(porta):
    gpio.output(porta, ligada)


# Metodo auxiliar para desligar uma porta
def desligar_porta(porta):
    gpio.output(porta, desligada)


def dois_segundos(porta):
    ligar_porta(porta)
    sleep(2)
    desligar_porta(porta)


def estado_verde():
    desligar_porta(porta_led_verde)
    desligar_porta(porta_led_amarelo)
    desligar_porta(porta_led_vermelho)
    desligar_porta(porta_campainha)
    ligar_porta(porta_led_verde)


def estado_amarelo():
    desligar_porta(porta_led_verde)
    desligar_porta(porta_led_amarelo)
    desligar_porta(porta_led_vermelho)
    desligar_porta(porta_campainha)
    ligar_porta(porta_led_amarelo)


def estado_vermelho():
    desligar_porta(porta_led_verde)
    desligar_porta(porta_led_amarelo)
    desligar_porta(porta_led_vermelho)
    desligar_porta(porta_campainha)
    ligar_porta(porta_led_vermelho)


def estado_campainha():
    desligar_porta(porta_led_verde)
    desligar_porta(porta_led_amarelo)
    desligar_porta(porta_led_vermelho)
    desligar_porta(porta_campainha)
    ligar_porta(porta_campainha)


def estado_desligado():
    desligar_porta(porta_led_verde)
    desligar_porta(porta_led_amarelo)
    desligar_porta(porta_led_vermelho)
    desligar_porta(porta_campainha)


def estado_completo():
    ligar_porta(porta_led_verde)
    ligar_porta(porta_led_amarelo)
    ligar_porta(porta_led_vermelho)
    ligar_porta(porta_campainha)
