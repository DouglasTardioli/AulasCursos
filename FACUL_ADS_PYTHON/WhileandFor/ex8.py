print('Primos de 2 até 99')

for numero in range(2, 100, 1):
    flag = 0
    for i in range(2, numero, 1):
        if (numero % i == 0):
            flag = 1
            break
    if not flag:
        print(numero)