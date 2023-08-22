print('CALCULADORA')


print('Escolha uma opção: ')
print('[s]air')


while True:
    print('+ - * /')
    operator = input('Escolha qual operação deseja: ')
    if operator == '+' or operator == '-' or operator == '*' or operator == '/':
        valor1 = float(input('Digite o primeiro número: '))
        valor2 = float(input('Digite o segundo número: '))

    if (operator == '+'):
        soma = valor1 + valor2
        print('a soma de {} + {} é igual a: {:.2f}'.format(valor1, valor2, soma))
        continue
    elif (operator == '-'):
        subtracao = valor1 - valor2
        print('a subtração de {} - {} é igual a: {:.2f}'.format(valor1, valor2, subtracao))
        continue
    elif (operator == '*'):
        multiplicacao = valor1 * valor2
        print('a Multiplicação de {} * {} é igual a: {:.2f}'.format(valor1, valor2, multiplicacao))
        continue
    elif (operator == '/'):
        divisao = valor1 / valor2
        print('a Divisão de {} / {} é igual a: {:.2f}'.format(valor1, valor2, divisao))
        continue
    elif (operator == 's' or operator == 'S'):
        break
    else:
        print('Operação incorreta!!')
        
print('Encerrando programa!!')