soma = 0
qtd = 0
for i in range(1,150):
    if(i % 2 == 0):
        soma += i
        qtd += 1
media = soma / qtd

print(f'A média dos pares de 1 até 150 é {media}')