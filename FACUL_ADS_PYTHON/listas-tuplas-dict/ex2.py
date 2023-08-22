game = {
    'nome': 'Super Mario',
    'desenvolvedora': 'Nintendo',
    'ano': 1990,
}

for key, value in game.items():
    print(f'{key} = {value}')

print()
print()

games = []

game1 = {
     'nome': 'Super Mario',
    'videogame': 'Super-Nintendo',
    'ano': 1990,
}
game2 = {
     'nome': 'Zelda Ocarina Of time',
    'videogame': 'Nintendo 64',
    'ano': 1998,
}
game3 = {
     'nome': 'Pokemon Wellow',
    'videogame': 'Game Boy',
    'ano': 1999,
}

games = [game1, game2, game3]

for i in games:
    print(i)

