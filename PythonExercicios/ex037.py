nota1 = float(input('Diga sua primeira nota '))
nota2 = float(input('Diga sua segunda nota '))
media = (nota1 + nota2) / 2
print('Sua media foi {} '.format(media))
if media < 5:
    print('Você esta REPROVADO!!'.format(media))
elif 5 <= media < 7:
    print('Você esta de RECUPERAÇÂO!!')
else:
    print('Parabéns vocé foi APROVADO!')
