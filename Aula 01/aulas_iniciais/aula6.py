# Interpolação básica de strings
# s - strings 
# d e i - int
# f - float
# x e X - hexadecimal(ABCDEF0123456789)

nome = "Douglas"
preco = 1000.54234

variavel = '%s, o preço é R$%.2f' % (nome, preco)

print(variavel)

print('O hexadecimal de %d é %08X' % (2600, 2600))