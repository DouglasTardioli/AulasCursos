# Formatação Básica de strings
# s - string
# d - int
# f - float
# .<número de dígitos>f
# > - esquerda
# < - direita
# ^ - Centro 
# Sinal - + ou -
# ex.: 0>100,.1f
# conversion flags - !r !s !a

Variavel = 'ABC'

print(f'{Variavel}')
print(f'{Variavel: >10}')
print(f'{Variavel: <10}.')
print(f'{Variavel:0^10}.')
print(f'{10000.439245252:.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')