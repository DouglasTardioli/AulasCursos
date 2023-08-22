print('Calculadora de consumo de Energia')
print('Tipos de Instalação: ')
print('r (residêncial)')
print('i (indústrial)')
print('c (comercial)')

tipo = input('clique na letra referente ao tipo de instalação: ')
if (tipo == 'r' or tipo == 'i' or tipo == 'c'):
    consumo = float(input('Qual o consumo em KWH: '))

if (tipo == 'r'):
    if (consumo <= 500):
        preco = 0.4
    else:
        preco = 0.65
elif (tipo == 'i'):
    if (consumo <= 5000):
        preco = 0.55
    else:
        preco = 0.60

elif (tipo == 'c'):
    if (consumo <= 1000):
        preco = 0.55
    else:
        preco = 0.60
else:
    print('OPÇÃO INVALIDA!!')

print('o Valor a ser pago é de: R${:.2f}'.format(consumo * preco))
