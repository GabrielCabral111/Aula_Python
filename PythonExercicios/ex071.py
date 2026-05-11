from random import randint
tupla = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print('Os numeros sortiados     ', end='')
for numero in tupla:
    print(f'{numero} ', end='')
print(f'\nO maior valor foi {max(tupla)}')
print(f'O menor valor foi {min(tupla)}')