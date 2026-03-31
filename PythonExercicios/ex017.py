import math

angulo = float(input('Digite um angulo qualquer: '))

seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O angulo {} tem o Seno de {}'.format(angulo, seno))
print('O angulo {} tem o Cosseno de {}'.format(angulo, cosseno))
print('O angulo {} tem o Tangente de {}'.format(angulo, tangente))