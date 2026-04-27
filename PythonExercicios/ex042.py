import random
from time import sleep

print('='*30)
print(""" JO kEN PO !!! """)
print('='*30)
print('Suas opções:')
print('-'*30)
print('[0] PEDRA')
print('[1] PAPEL')
print('[2] TESOURA')
jogada = ('PEDRA', 'PAPEL', 'TESOURA')
play1 = random.randint(0, 2)
play2 = int(input('Qual e sua jogada '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO ....')
print('-=-'*20)
print('O Computador escolheu {}'.format(jogada[play1]))
print('O Jogador escolheu {}'.format(jogada[play2]))
print('-=-'*20)
if play1 == 0:# Computador Jogou Pedra
    if play2 == 0:
        print('EMPATE !')

    elif play2 == 1:
        print('VOCÊ VENCEU !')

    elif play2 == 2:
        print('COMPUTADOR VENCEU !')

    else:
        print('Jogada INVALIDA !!')

elif play1 == 1: # Computador Jogou Papel
    if play2 == 0:
        print('COMPUTADOR VENCEU !')

    elif play2 == 1:
        print('EMPATE !')

    elif play2 == 2:
        print('VOCÊ VENCEU !')

    else:
        print('Jogada INVALIDA !')

elif play1 == 2: # Computador Jogou Tesoura
    if play2 == 0:
        print('VOCÊ VENCEU !')

    elif play2 == 1:
        print('COMPUTADOR VENCEU !')

    elif play2 == 2:
        print('EMPATE !')
    else:
        print('Jogada INVALIDA !')



