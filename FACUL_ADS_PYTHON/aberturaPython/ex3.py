km = float(input('Quantos KM vc percorreu: '))
dias = int(input('Quantos dias vc usou o carro: '))

precoPagar = (km * 0.15) + (dias * 60)

print('vc percorreu {}km e alugou por {} dias, total a pagar: {}'.format(km, dias, precoPagar))