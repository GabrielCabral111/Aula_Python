import random

print('-'*30)
print("""   @@@@ Jogo da sorte @@@@
teste para saber se voce ganha da maquina
    Escolha um numero de 0 a 5 """)
num1 = int(input('Digite um numero : '))
sorte = random.randint(0,5)
print('O numero que voce colocou foi {} \ne o que a maquina escolheu foi {}'.format(num1,sorte))
if sorte == num1:
    print('Você acertou parabens !')
else:
    print('Você errou tente novamente')
