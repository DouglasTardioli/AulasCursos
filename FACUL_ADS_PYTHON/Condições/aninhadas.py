#Condições aninhadas (if dentro de outros)
print('Escolha o que deseja Comprar: ')
print('1 - Maça')
print('2 - Laranja')
print('3 - Banana')
produto = int(input('Qual a sua escolha? '))
qtd = int(input('Quantas Unidades? '))

if (produto == 1) :
    pagar = qtd * 2.3
    print('Vc comprou {} maças. Total à pagar: {}'.format(qtd, pagar))
elif (produto == 2) :
    pagar = qtd * 3.6
    print('Vc comprou {} Laranjas. Total à pagar: {}'.format(qtd, pagar))
elif (produto == 3) :
    pagar = qtd * 1.85
    print('Vc comprou {} Bananas. Total à pagar: {}'.format(qtd, pagar))
else:
    print('Produto Inexistente!!')