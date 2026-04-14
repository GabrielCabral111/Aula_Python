import datetime

ano_Nascimento = int(input('Digite o ano de nascimento: '))
idade = datetime.date.today().year - ano_Nascimento
if idade == 18 :
    print('ESTA NA HORA DE VOCÊ SE ALISTA ')
elif idade < 18:
    print('SUA IDADE É {}, NÃO PODE SE ALISTA AINDA FALTA {} ANO PARA VOCÊ SE ALISTAR '.format(idade,  18 - idade))

else:
    print('SUA IDADE E {} VOCÊ JA PASSOU DA DATA POR {} ANOS '.format(idade, idade - 18))