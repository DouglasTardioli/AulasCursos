print()
print()

game = {}
games = []

for i in range(3):
    game['Nome']= input('QUal o nome do jogo: ')
    game['Videogame']= input('Qual o videoGame: ')
    game['ano']= input('Qual o ano de lançamento: ')
    games.append(game.copy())
print('-' * 20)
for e in games:
    for key, value in e.items():
        print(f'O campo {key} tem o valor {value}.')