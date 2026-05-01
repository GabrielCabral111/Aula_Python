n = 0
s = 0
cont = 0
while n <=999:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    else:
        s += n
        cont += 1
print('Você digitou {} numeros e a soma entre eles foi {}'.format(cont, s))