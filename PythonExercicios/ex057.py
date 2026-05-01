import math
numero = int(input('Digite um numero inteiro: '))
cont = numero
while cont > 0:
    print('{}'.format(cont), end='')
    print(' x '  if cont > 1 else '= {}'.format(math.factorial(numero)) ,end='')
    cont -= 1