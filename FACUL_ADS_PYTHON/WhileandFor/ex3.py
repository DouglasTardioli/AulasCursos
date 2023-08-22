x = float(input('Digite um valor: '))
y = float(input('Digite outro valor: '))

count = 1
multi = 0

while (count <= x):
    multi += y
    count += 1
print(f'resultado da Multiplicação: {x}x{y} = {multi:.2f}')