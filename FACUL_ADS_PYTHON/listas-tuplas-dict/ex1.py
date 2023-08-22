item = []
mercado = []

for i in range(3):
    item.append(input('Digite o nome do item: '))
    item.append(int(input('Digite a quantidade: ')))
    item.append(float(input('Digite o valor: ')))
    mercado.append(item[:])
    item.clear()


# [:] = COPIAR
print()
print()
print()
soma = 0
print('Lista de Compras: ')
print('-' * 20)
print('Item | Quantidade | Valor Unitario | Valor do Item')
for item in mercado:
    print(f'{item[0]} | {item[1]} | {item[2]} |{item[1] * item[2]:.2f}')
    soma += item[1] * item[2]
print('-' * 20)
print('Total a ser pago: {}'.format(soma))
