from datetime import date

print('='*30)
print(""" Confederaçãoo de Natação""")
print('='*30)
ano = int(input('Digite o ano de nascimento: '))
idade = date.today().year - ano
print('Você tem {} anos e um : '. format(idade))
if idade <= 9 :
    print('Atleta MIRIM')
elif idade <= 14 :
    print('Atleta INFANTIL')
elif idade <= 19 :
    print('Atleta Junior')
elif idade <= 25 :
    print('Atleta SÊNIOR')
else:
    print('Atleta MASTER')
print('='*30)