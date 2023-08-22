
def volumeFeijoada():
    print('-' * 20, 'Menu 1 de 3 - Volume feijoada', '-' * 20)
    while True:
        try:     
            volumeF = int(input('Qual a quantidade desejada (ml): '))
            if volumeF >= 300 and volumeF <= 5000:
              return volumeF * 0.08
            else:
                print('Valores aceitos: 300ml a 5000ml.')
        except ValueError:
            print('Por favor, digite valores inteiros.')

def opcaoFeijoada():
    print('-' * 20, 'Menu 2 de 3 - Opção feijoada', '-' * 21)
    while True:
        opcaoF = input('Escolha a opção de feijoada \n' +
                       'b - (Feijão + paiol + costelinha) \n' + 
                       'p - Premium (Feijão + Paiol + costelinha + partes de porco) \n' +
                       's - Suprema (Feijão + Paiol + costelinha + partes de porco + charque + calabresa + bacon) \n' +
                       '>> ')
        opcaoF = opcaoF.lower().strip()
        if opcaoF == 'b':
            return 1.00
        elif opcaoF == 'p':
            return 1.25
        elif opcaoF == 's':
            return 1.50
        else:
            print('Digite uma das opções acima. (b, p, s)')
            continue
def acompanhamentoFeijoada():
    print('-' * 20, 'Menu 1 de 3 - Acompanhamento feijoada', '-' * 12)
    accum = 0
    while True:
        acompanhamentoF = input('Deseja mais algum acompanhamento: \n' +
                                '0 - Não desejo mais acompanhamentos (encerrar pedido) \n'+
                                '1 - 200g de arroz\n'+
                                '2 - 150g de farofa especial\n'+
                                '3 - 100g de couve cozida\n'+
                                '4 - 1(uma) laranja descascada\n' +
                                '>> ' )
        if acompanhamentoF == '0':
            return accum
        elif acompanhamentoF == '1':
            accum += 5
            continue
        elif acompanhamentoF == '2':
            accum += 6
            continue
        elif acompanhamentoF == '3':
            accum += 7
            continue
        elif acompanhamentoF == '4':
            accum += 3
            continue
        else:
            print('Digite as opções acima.')
 

print('-' * 20, 'Bem-vindo ao programa de Feijoada do Douglas Peixoto Tardioli' ,'-' * 20)
preco_volume = volumeFeijoada()

opcao = opcaoFeijoada()


acompanhamentoF = acompanhamentoFeijoada()
total = (preco_volume * opcao) + acompanhamentoF
print(f'o Total ficou: R${total:.2f} (volume: R${preco_volume}. Opção: R${opcao:.2f}. acompanhamento: R${acompanhamentoF:.2f}.)')
