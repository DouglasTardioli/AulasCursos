def validad_int(pergunta, min, max):
    x = int(input(pergunta))
    while (x < min or x > max):
        x = int(input(pergunta))
    return x
print('Cadastro de jogos e consoles. 🎮')

def criarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'wt+')
        a.close()
    except:
        print('ERROR Na criação do arquivo')
    else:
        print(f'Arquivo {nomeArquivo} foi criado com sucesso!!\n')

def existeArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True   

def cadastrarJogo(nomeArquivo, nome_jogo, nome_console):
    try:
        a = open(nomeArquivo, 'at')
    except:
        print('Erro ao abrir o arquivo')
    else:
        a.write(f'{nome_jogo};{nome_console}\n')
    finally:
        a.close()

def listarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
    except:
        print('Erro ao abrir o arquivo')
    else:
        print(a.read())
    finally:
        a.close()

arquivo = 'games.txt'
if existeArquivo(arquivo):
    print('Arquivo Localizado no computador.')
else:
    print('Arquivo inexistente.')
    criarArquivo(arquivo)

while True:
    print('Menu')
    print('1 - Cadastrar nome do Jogo/console.')
    print('2 - Listar jogos.')
    print('3 - Sair.')
    
    op = validad_int('Escolha a opção desejada: ', 1, 3)
    if op == 1:
        print('Opçao de cadastrar selecionada...\n')
        nome_jogo = input('Nome do jogo: ')
        nome_console = input('Nome do Console: ')
        cadastrarJogo(arquivo, nome_jogo, nome_console)
            
    elif op == 2:
        print('Opçao de Listar selecionada...\n')
        listarArquivo(arquivo)
    elif op == 3:
        print('Escerrando o programa...')
        break