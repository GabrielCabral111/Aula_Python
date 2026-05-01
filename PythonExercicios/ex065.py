from random import randint

vitoria = 0
while True:
    jogador = int(input('Escolha um numero:'))
    computador = randint(0, 10)
    parOupar = str(input('Voce deseja Par ou Impar? [P/I] ')).strip().upper()[0]
    soma = computador + jogador
    while parOupar not in 'PI':
        parOupar = str(input('Digite novamente deseja Par ou Impar? [P/I] ')).strip().upper()[0]
    print('-' * 20)
    print(f'Voce jogou {jogador} e o computador {computador}. Total deu {soma} |', end=' ')
    print('DEU PAR' if soma % 2 == 0 else 'DEU IMPAR')
    print('-' * 20)
    if parOupar == 'P' :
        if soma % 2 == 0:
            vitoria += 1
            print('Você venceu !')
            print('Vamos jogar novamente...')
            print('-' * 20)
        else:
            print('Você Perdeu ......')
            break
    elif parOupar == 'I' :
        if soma % 2 == 1:
            vitoria += 1
            print('Você venceu ! ......')
            print('Vamos jogar novamente...')
            print('-' * 20)
        else:
            print('Você Perdeu ......')
            break
    print('Stop para encerrar...')

print('-=-' * 20)
print('{:=^30}'.format(' Fim Do Jogo '))
print(f'GAME OVER ! Você venceu {vitoria} vezes')







