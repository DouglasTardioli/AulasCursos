numeroStr = input('Vou dobrar o número que vc digitar: ')

try: 
  print('STR: ', numeroStr)
  numeroFloat = float(numeroStr)
  print('FLOAT: ', numeroFloat)
  print(f'O dobro de {numeroStr} é {numeroFloat *2:.2f}')
except:
  print('Isso não é um número')