nu1 =  int(input('Digite um numero :'))
nu2 = int(input('Digite o segundo numero :'))
nu3: int = int(input('Digite terceiro numero :'))
# verificando maior
maior = nu1
if nu2 > maior:
    maior = nu2
if nu3 > maior:
    maior = nu3
# verificando menos
menor = nu1
if nu2 < menor:
    menor = nu2
if nu3 < menor:
    menor = nu3
print('O numero mairo é {}'.format(maior))
print('O numero menor é {}'.format(menor))