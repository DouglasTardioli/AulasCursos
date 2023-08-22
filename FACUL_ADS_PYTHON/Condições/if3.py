#NOT, AND, OR
#NOT Inverte os valores true ou false
#AND só resulta em True caso ambas entradas sejam TRUE
#OR só resulta se uma entrada for TRUE
nota1 = float(input('Digite sua nota de Matematica: '))
nota2 = float(input('Digite sua nota de Quimica: '))
nota3 = float(input('Digite sua nota de Fisica: '))

if nota1 >= 7 and nota2 >= 7 and nota3 >= 7 : 
    print('Parabenssss, vc passou de ano!!')
else:
    print('REPROVADO!!!')