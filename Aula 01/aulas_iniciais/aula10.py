velocidade = 60
localCarro = 90

RADAR_1 = 60
LOCAL_1= 100
RADAR_RANGE = 1

if velocidade > RADAR_1:
    print('Velocidade Carro passou do radas 1')

if localCarro >= (LOCAL_1 - RADAR_RANGE) and \
    localCarro <= (LOCAL_1 + RADAR_RANGE) and \
      velocidade > RADAR_1:
    print('carro multado em radar 1')