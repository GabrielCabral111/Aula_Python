import random

print('-'*30)
print('Sou seu computador ...')
print('Acabei de pensar em um numero inteiro de 0 a 10')
print('Será que você consegue adivinhar?')
print('-'*30)
sorte = random.randint(1,10)
numero = 0
cont = 0
while numero != sorte:
    numero = int(input('Qual e o seu palpite?: '))
    if sorte > numero:
        print('Mais... tente novamente')
    elif sorte < numero:
        print('Menos... tente novamente')
    cont += 1
print('Acertou .... foi com {} tentativas. Parabens \ne o que a maquina escolheu foi {}'.format(cont,sorte))

