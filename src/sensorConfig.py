
# Endereço I2C do TCS34725
TCS34725_I2C_ADDR = 0x29

# Controle do sensor
TCS34725_CMD = 0x80
TCS34725_CMD_AUTO_INC = 0xA0

# Registros do sensor
TCS34725_REG_ENABLE = 0x00
TCS34725_REG_ATIME = 0x01
TCS34725_REG_CONTROL = 0x0F
TCS34725_REG_CDATAL = 0x14
TCS34725_REG_CDATAH = 0x15
TCS34725_REG_RDATAL = 0x16
TCS34725_REG_RDATAH = 0x17
TCS34725_REG_GDATAL = 0x18
TCS34725_REG_GDATAH = 0x19
TCS34725_REG_BDATAL = 0x1A
TCS34725_REG_BDATAH = 0x1B

# Configuração do sensor
def configure_sensor(i2c):
    i2c.writeto_mem(TCS34725_I2C_ADDR, TCS34725_REG_ENABLE | TCS34725_CMD, bytes([0x03]))  
    i2c.writeto_mem(TCS34725_I2C_ADDR, TCS34725_REG_ATIME | TCS34725_CMD, bytes([0xEB]))

# Operação de leitura das cores
def escanear_cores(i2c):
    cor_escaneada = i2c.readfrom_mem(TCS34725_I2C_ADDR, TCS34725_REG_CDATAL | TCS34725_CMD_AUTO_INC, 8)
    clear = cor_escaneada[1] << 8 | cor_escaneada[0]
    vermelho = cor_escaneada[3] << 8 | cor_escaneada[2]
    verde = cor_escaneada[5] << 8 | cor_escaneada[4]
    azul = cor_escaneada[7] << 8 | cor_escaneada[6]

    return clear, vermelho, verde, azul

