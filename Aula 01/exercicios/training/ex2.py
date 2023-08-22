def multiplicar (*args):
    total = 1
    for numero in args:
        total *= numero
    return total
multiplicacao = multiplicar(1, 2, 3, 4, 5, 6)
print(multiplicacao)

def par_impar(numero):
    par = numero % 2 == 0
    if par:
        return f'{numero} é par'
    return f'{numero} é ímpar'

print(par_impar(2))
print(par_impar(3))
print(par_impar(4))
print(par_impar(15))
        