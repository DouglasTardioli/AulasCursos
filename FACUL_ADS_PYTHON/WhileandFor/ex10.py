frase = input('Digite uma frase: ')
tamanho = len(frase)
while (tamanho < 10 or tamanho > 30):
    frase: input('Digite uma frase: ')
    tamanho = len(frase)
print(f'Com espaços: {frase}')
print('Sem espaços: ', end="")
for i in range(0, tamanho, 1):
    if (frase[i] != ' '):
        print(frase[i], end='')