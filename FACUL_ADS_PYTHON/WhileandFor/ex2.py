soma = 0
count = 1

while (count <= 5):
    x = float(input(f'Digite o {count}° número: '))
    soma = soma + x
    count += 1
print(f'Somatório: {soma}')