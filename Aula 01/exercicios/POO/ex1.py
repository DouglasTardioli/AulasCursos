import json

CAMINHO_ARQUIVO = 'aula1.json'


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
p1 = Pessoa('Anakin', 25)
p2 = Pessoa('Luke', 30)
p3 = Pessoa('Leia', 46)
db = [vars(p1), p2.__dict__, vars(p3)]

def fazer_dump():
  with open(CAMINHO_ARQUIVO, 'w') as arquivo:
      json.dump(db, arquivo, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    fazer_dump()