idade = int(input('Qual a sua idade? '))
while (idade > 0): 
    sexo = input('Qual o seu sexo? (M ou F): ')
    if (sexo == 'M' or sexo == "m"):
        print(f'Boa noite, Senhor. sua idade é {idade}')
        break
    elif (sexo == 'F' or sexo == 'f'):
         print(f'Boa noite, Senhora. sua idade é {idade}')
         break
    else:
        print('Opção de sexo inexistene.')
    idade = int(input('Qual sua idade?'))
print('Encerrando...')
