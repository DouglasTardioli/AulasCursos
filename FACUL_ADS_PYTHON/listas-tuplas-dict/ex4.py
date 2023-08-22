
# COMEÇA COM --
s1 = 'Lógica de programação e algoritmos'
print(s1.startswith('Lógica'))

# TERMINA COM --
s1 = 'Lógica de programação e algoritmos'
print(s1.endswith('algoritmos'))

# LOWER = miniscula -- UPPER = maiuscula --
s1 = 'Lógica de programação e algoritmos'
print(s1.lower().endswith('algoritmos'))

# Contagem de caracter
s1 = 'Lógica de programação e algoritmos'
print(s1.lower().count('a'))

#Substitui strings
s1 = 'Lógica de programação e algoritmos'
print(s1.replace('Lógica', 'fundamentos'))

"""
Retorna TRUE para string
isalnum
isalpha
isdigit
isnumeric
isupper
islower
isspace
isprintable
"""

s1 = 'Lógica de programação e algoritmos'
s2 = '42'

#Somente LEtras e Numeros
print(s1.isalnum())
print(s2.isalnum())

#Somente LEtras
print(s1.isalpha())
print(s2.isalpha())

# Numero
print(s1.isdigit())
print(s2.isdigit())
