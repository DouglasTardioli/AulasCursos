a = int(input('Digite o primeiro lado do triângulo: '))
b = int(input('Digite o segundo lado do triângulo: '))
c = int(input('Digite o terceiro lado do triângulo: '))

if (a > 0 and b > 0 and c > 0):
    if (a + b > c and a + c > b and b + c > a):
      if (a != b and a != c and b != c):
        print('Triângulo Escaleno!')
      elif (a == b and a == c and b == c ):
         print('Triângulo equilátero!')
      else:
         print('Triângulo isósceles!')
    else:
        print('Ao menos um dos valores indicados não servem para formar o triângulo')
else:
    print('Ao menos um dos valores indicados não servem para formar o triângulo')