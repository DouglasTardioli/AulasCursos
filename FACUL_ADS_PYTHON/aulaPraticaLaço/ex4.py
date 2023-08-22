
total = 0
dinheiro = 0

while True:
    print('Calcule o preço dos ingressos.')
    print('[S]air')
    idade = input('Qual sua idade? ')
    if idade == 's' or idade == 'S':
        break
    idade = int(idade)
    total += 1
    if idade <= 3:
        ingresso = 0
    elif idade > 12:
        ingresso = 15
    else:
        ingresso = 302

    dinheiro += ingresso
    
media = dinheiro / total    
print(f'Total de pessoas: {total}')   
print(f'Você pagará: R${dinheiro}')    
print(f'Média de idade: {media:.1f}')    

print('Saindo...')