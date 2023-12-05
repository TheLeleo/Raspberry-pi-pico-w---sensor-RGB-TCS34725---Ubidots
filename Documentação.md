# Diagrama de Blocos: Comunicação I2C entre Raspberry Pi Pico e Sensor TCS34725

O diagrama de blocos abaixo ilustra a conexão e a comunicação I2C entre o Raspberry Pi Pico e o sensor de cor TCS34725. Ele apresenta os principais componentes e as conexões necessárias para a leitura das cores por meio do protocolo I2C.


## Descrição dos Componentes:

### Raspberry Pi Pico:
- Microcontrolador responsável por controlar o processo de leitura do sensor.
- Gerencia a comunicação I2C com o sensor TCS34725.

### Sensor TCS34725:
- Sensor de cor que mede as intensidades de luz nas faixas vermelha, verde e azul.
- Possui um endereço I2C específico para comunicação.

## Conexões:

### SDA (Serial Data):
- Conecta o pino SDA do Raspberry Pi Pico ao pino correspondente no sensor TCS34725.
- Canal de comunicação bidirecional para a transferência de dados.

### SCL (Serial Clock):
- Conecta o pino SCL do Raspberry Pi Pico ao pino correspondente no sensor TCS34725.
- Canal de comunicação unidirecional para sincronização de dados.

## Funcionamento:

1. O Raspberry Pi Pico inicia a comunicação I2C com o sensor TCS34725.
2. A função `configure_sensor` é chamada para enviar comandos de configuração ao sensor.
3. O loop principal no arquivo `main.py` chama a função `escanear_cores` para realizar leituras periódicas das cores.
4. Os dados lidos são processados e normalizados.
5. As informações normalizadas são enviadas para o servidor Ubidots usando a função `POST` no arquivo `conexao.py`.

Este diagrama de blocos representa uma visão simplificada da comunicação I2C entre o Raspberry Pi Pico e o sensor TCS34725, fornecendo uma base para entender a interação entre os componentes no sistema.

