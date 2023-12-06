# Descrição de comunicação I2C entre microcontrolador e sensor de comunicação serial

## Comunicação I2C entre Raspberry Pi Pico e Sensor TCS34725

A comunicação I2C (Inter-Integrated Circuit) é um protocolo serial utilizado para a comunicação entre microcontroladores e periféricos. No caso do Raspberry Pi Pico e do sensor TCS34725, a comunicação ocorre por meio de dois fios: SDA (Data) e SCL (Clock).

### Configuração do Sensor

Antes de iniciar a comunicação, é necessário configurar o sensor TCS34725. A função `configure_sensor` realiza essa configuração, enviando comandos e valores específicos para os registradores do sensor via I2C.

- **Endereço I2C do TCS34725:** 0x29
- **Controle do Sensor (Comando):** 0x80
- **Registro de Controle Automático Incremental:** 0xA0
- **Registros do Sensor:**
  - Registro de Habilitação (ENABLE): 0x00
  - Registro de Integração de Tempo (ATIME): 0x01

### Leitura das Cores

A função `escanear_cores` é responsável por realizar a leitura das cores do ambiente por meio do sensor TCS34725. Os valores lidos incluem a intensidade de luz clara (clear) e as intensidades de vermelho, verde e azul.

- **Registro de Dados (CDATAL, CDATAH, RDATAL, RDATAH, GDATAL, GDATAH, BDATAL, BDATAH):** 0x14 a 0x1B

Os dados lidos são então processados para obter valores proporcionais às intensidades das cores RGB (vermelho, verde, azul).

## Comunicação Serial entre Raspberry Pi Pico e PC

A comunicação serial é um meio de transferir dados em série entre dispositivos. No caso do Raspberry Pi Pico e do PC, essa comunicação é utilizada para enviar informações sobre as leituras de cores para um servidor MQTT hospedado na plataforma Ubidots.

### Configuração da Comunicação MQTT

O arquivo `conexao.py` contém funções para estabelecer a conexão Wi-Fi e publicar os dados no servidor MQTT da Ubidots. Aqui estão os principais pontos:

- **Cliente MQTT:** Utiliza a biblioteca `umqtt.simple` para criar um cliente MQTT.
- **Configuração:** Define o servidor, porta, chave da Ubidots e informações de Wi-Fi.
- **Conexão:** Estabelece a conexão Wi-Fi e, em seguida, a conexão MQTT.
- **Publicação:** Publica os dados no tópico especificado (`ROTA`) no formato JSON.

### Integração com o Sensor e Loop Principal

O arquivo `main.py` integra a leitura do sensor com a comunicação MQTT. No loop principal:

- As cores são lidas do sensor usando funções do arquivo `sensorConfig.py`.
- As intensidades de cada cor são normalizadas e convertidas para um código hexadecimal.
- Um JSON é construído com os dados normalizados de intensidade vermelha e enviado para o servidor Ubidots usando a função `POST` do arquivo `conexao.py`.

Essa integração permite monitorar e visualizar as leituras do sensor em tempo real na plataforma Ubidots, proporcionando uma solução completa de IoT utilizando o Raspberry Pi Pico.
