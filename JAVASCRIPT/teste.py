import random

qtd = 0
ddd = 11

quantidade = int(input('quantas vezes deseja gerar os números?: '))
while True:
        randomNumber = random.randint(10000000, 99999999)
        print(f'wa.me/55{ddd}9{randomNumber}\n')
        qtd = qtd + 1
        
        if qtd > (quantidade - 1):
                break



