print('Calcule quantas cédulas precisará')
valor = int(input('Digite o valor em R$ '))

while True:
  if valor >= 100:
      cedulas100 = valor // 100
      valor -= cedulas100 * 100
      print(f'Cédulas de 100: {cedulas100}')
      if not valor:
          break
  if valor >= 50:
      cedulas50 = valor // 50
      valor -= cedulas50 * 50
      print(f'Cédulas de 50: {cedulas50}')
      if not valor:
          break
  if valor >= 20:
      cedulas20 = valor // 20
      valor -= cedulas20 * 20
      print(f'Cédulas de 20: {cedulas20}')
      if not valor:
          break
  if valor >= 10:
      cedulas10 = valor // 10
      valor -= cedulas10 * 10
      print(f'Cédulas de 10: {cedulas10}')
      if not valor:
          break
  if valor >= 5:
      cedulas5 = valor // 5
      valor -= cedulas5 * 5
      print(f'Cédulas de 5: {cedulas5}')
      if not valor:
          break
  if valor:
      cedulas1 = valor
      print(f'Cédulas de 1: {cedulas1}')
      break