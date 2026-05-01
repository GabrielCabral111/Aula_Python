'''c = 1
while c < 10:
    print(c)
    c += 1
print('FIM')'''

'''while n != 0 :
    n = int(input('digite um numero: '))
print('FIM') '''
n = 1
r = ''
'''while r == 'S':
    n = int(input('digite um numero: '))
    r = str(input('Quer continuar? [S/N] : ')).strip().upper()
print('FIM')
soma = 0'''
par = 0
impar = 0
while n != 0 :
    n = int(input('digite um numero: '))
    if n != 0 :
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Vocé digitou {} numeros Par e {} numeros Impar'.format(par, impar))
