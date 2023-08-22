print('Calcule seu desconto')
print('Loja do Douglas Tardioli')

valor_produto = float(input('Entre com o valor desejado: R$'))
qtd_produto = int(input('Qual a quantidade do produto: '))

valor_total = valor_produto * qtd_produto

if (qtd_produto <= 4):
    print('o valor do produto é de: R${}'.format(valor_total))
    print('Sem desconto para esta quantidade!')

      #DESCONTO_DE_3%
elif (qtd_produto >= 5 and qtd_produto <= 19):
    print('o valor total é de: R${}'.format(valor_total))
    desconto = valor_total * 0.03
    desconto_pagar = valor_total - desconto
    print('Desconto calculado de R${:.2f}'.format(desconto))
    print('o valor com desconto é de: R${} (desconto de 3%)'.format(desconto_pagar))

    #DESCONTO_DE_6%
elif (qtd_produto >= 20 and qtd_produto <= 99):
    print('o valor total é de: R${}'.format(valor_total))
    desconto = valor_total * 0.06
    desconto_pagar = valor_total - desconto
    print('Desconto calculado de {:.2f}'.format(desconto))
    print('o valor com desconto é de: R${} (desconto de 6%)'.format(desconto_pagar))

        #DESCONTO_DE_10%
else:
    print('o valor total é de: R${}'.format(valor_total))
    desconto = valor_total * 0.10
    desconto_pagar = valor_total - desconto
    print('Desconto calculado de {:.2f}'.format(desconto))
    print('o valor com desconto é de: R${} (desconto de 10%)'.format(desconto_pagar))