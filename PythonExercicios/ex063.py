n = 0
s = 0
cont = 0
while n != 999:
    n = int(input('Digite um numero: para par digite [999]  '))
    if n == 999:
        break
    s += n
    cont+=1
print(' Voce digitou {} numeros e a soma de cada um foi {}'.format(cont, s))