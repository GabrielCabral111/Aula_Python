n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))

so = n1 + n2
su = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma vale {}'.format(so))
print('A soma é {}, a subtração é {}, a multiplicação é {} e a divisão é {:.3f}'.format(so, su, m, d))
print('Divisão inteira é {} e a potência é {}'.format(di, e))