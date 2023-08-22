# Manipulação de Strings/array

frase = input('Digite uma frase: ')
tam = len(frase)

fraseMetade = frase[:int(tam/2)]
fraseUltimos = fraseMetade[-2:]
print(fraseMetade, fraseUltimos)