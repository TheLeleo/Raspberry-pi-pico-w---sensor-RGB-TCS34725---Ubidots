from umqtt.simple import MQTTClient
import network
import utime

ROTA = b'/v1.6/devices/rgb-color'

SERVER = 'industrial.api.ubidots.com'
PORTA = 1883
CHAVEUBIDOTS = 'BBUS-R0PI1FARBEhSFtysKBem0dPYwuvG7q'

WIFI_NOME = 'SHARE-RESIDENTE'
WIFI_SENHA = 'Share@residente23'

TEMPO_MAX_CONEXAO = 60 

def POST(dados_de_post):
    conectar_ao_wifi()
    fazer_publicacao(dados_de_post)

def conectar_ao_wifi():
    sessao = network.WLAN(network.STA_IF)
    sessao.active(True)
    sessao.connect(WIFI_NOME, WIFI_SENHA)
    inicio_con = utime.time()

    print('Aguardando conexão Wi-fi')
    while not sessao.isconnected():
        if utime.time() - inicio_con > TEMPO_MAX_CONEXAO:
            print('Erro: Conexão não realizada.')
            break
        print('.')
        utime.sleep(1)

    if sessao.isconnected():
        print('Conexão realizada com sucesso:', sessao.ifconfig())

def fazer_publicacao(postagem):
    client = MQTTClient(
        client_id='umqtt_client',
        port=PORTA,
        user=CHAVEUBIDOTS,
        server=SERVER,
        password=''
    )

    client.connect()
    client.publish(ROTA, postagem)
    client.disconnect()

