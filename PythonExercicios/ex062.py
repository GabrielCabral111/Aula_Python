p = ''
n = 0
s = 0
media = 0
cont = 0
maior = 0
menor = 1
while not p == 'N':
    n = float(input('Digite um numero: '))
    s += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    p = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = s / cont
print('Você Digitou {} e a media foi {} '.format(cont, media))
print('O maior valor e {} e o menor foi {}'.format(maior, menor))