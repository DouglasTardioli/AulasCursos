# Operadores Lógicos
# and (e) or (ou) not (não)
# and - todas as condições precisam ser verdadeiras
# se qualquer valor for considerado falso,
# a expressão inteira será avalidada naquele Valor 
# são considerados falsy
# 0 0.0 '' False
# também existe o tipo none que é usado para representar um não Valor



#Exemplo AND
entrada = input('[E]ntrar [S]air: ')
senhaDigitada = input('Senha: ')

senhaPermitida = '123456'

if entrada == 'E' and senhaDigitada == senhaPermitida: 
  print("Entrou")
else: 
  print('Sair')
