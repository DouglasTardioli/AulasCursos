inicio = int(input('Digite um valor inicial: '))
fim = int(input('Digite um valor final: '))
qtd_positivo = 0
qtd_par = 0
qtd_impar = 0
soma_positivo = 0
soma_par = 0
soma_impar = 0
count = inicio

if (inicio < fim):
    while (count <= fim):
        if (count > 0):
            qtd_positivo += 1
            soma_positivo += count
        if (count & 2 == 0):
            qtd_par += 1
            soma_par += count
        else:
            qtd_impar += 1
            soma_impar += count
        count += 1
media_positivo = soma_positivo / qtd_positivo
media_par = soma_par / qtd_par
media_impar = soma_impar / qtd_impar

print(f'Quantidade de valores posítivos: {qtd_positivo:.2f}')
print(f'Media de valores posítivos: {media_positivo:.2f}')
print(f'Quantidade de valores pares: {qtd_par:.2f}')
print(f'Media de valores pares: {media_par:.2f}')
print(f'Quantidade de valores impares: {qtd_impar:.2f}')
print(f'media de valores impares: {media_impar:.2f}')