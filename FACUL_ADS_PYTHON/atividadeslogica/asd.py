print('Bem-vindo a Loja Micaela Milman')
print('Vamos calcular o seu desconto!')
#valor unitário:
unit = float(input('Qual valor do produto: R$ '))
#quantidade de produtos:
quant = float(input('Qual a quantidade de produtos: '))
#preço total do produto SEM desconto:
total = unit * quant
print(f'O valor do produto SEM desconto é: R${total:.2f}')
# se a quant for < que 200 unid
if quant <200:
    print('Desconto permitido somente acima de 200 unidades.')
# se a quant for >+ que 200 e < que 1000 unid
elif quant >= 200 and quant < 1000:
    desc = total - (total*0.05)
    print(f'O valor do produto COM 5% de desconto é: R${desc:.2f}')
#se a quant for >=1000 e > 2000 unid
elif quant >= 1000 and quant <2000:
    desc = total - (total*0.10)
    print(f'O valor do produto COM 10% de desconto é: R${desc:.2f}')
#se a quant >=2000
else:
    quant >=2000
    desc = total - (total*0.15)
    print(f'O valor do produto COM 15% de desconto é R${desc:.2f}')
print('Obrigada, volte sempre!')


