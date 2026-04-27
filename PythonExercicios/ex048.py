print('{:=^40}'.format(' 10 TERMOS DE UMA PA '))
num = int(input('Primeiro termo: '))
num2 = int(input('Qual e a razão termo: '))
decimo = num + (10 - 1) * num2
for c in range(num, decimo + num2 , num2):
    print('{} '.format(c), end=' -> ')
print(' ACABOU !!!!')