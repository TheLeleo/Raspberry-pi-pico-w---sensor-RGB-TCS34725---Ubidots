from machine import I2C, Pin
import utime
from sensorConfig import *
from conexao import POST

# comunicação I2C
i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=400000)

# Configurar sensor i2c
configure_sensor(i2c)

def converterParaHex(r, g, b):
    cor = "#{:02x}{:02x}{:02x}".format(int(r), int(g), int(b))
    return cor

# loop de execução do programa
while True:
    clear, vermelho, verde, azul = escanear_cores(i2c)
    
    media = (vermelho + verde + azul)/3
    
    r = (vermelho/media)*100
    g = (verde/media)*100
    b = (azul/media)*100
    print('R', r, 'G', g, 'B', b, 'clear', clear)
    
    hex_code = converterParaHex(r, g, b)
    print(hex_code)
    
    dados_de_post = '{"lelis": ' + str(r) + '}'
    POST(dados_de_post)
    
    utime.sleep(1)


