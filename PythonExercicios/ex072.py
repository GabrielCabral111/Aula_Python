tupa = ()
par = ()
nove = 0
for c in range (0, 4):
    numero = int(input('Digite um numero : '))
    tupa += (numero,)
    if numero % 2 == 0:
        par += (numero,)
print(f'Voce digitou os numeros {tupa}')
print(f'O numero 9 apareceu {tupa.count(9)} vezes')
if 3 in tupa:
    print(f'O valoe 3 apareceu na posição {tupa.index(3)}')
else:
    print('O valoe 3 apareceu não foi digitado')
print(f'os numeros par digitados foram {par}')