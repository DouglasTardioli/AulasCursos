price = float(input('Qual o preço do Produto: '))
desconto = float(input('Qual o desconto (%): '))
p = price * (desconto / 100)
priceComDesconto = price - p
mostrar = ('o Valor é de {} com desconto de {}%, ficará: {}'.format(price, desconto, priceComDesconto))

print(mostrar)