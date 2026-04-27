num =int(input('Digite um numeor :'))
contador = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m', end='')
        contador += 1
    else:
        print('\033[31m',end='')
    print('{}'.format(c), end=' ')
print('\n \033[m O numero {} foi Divizivel {} vezes '.format(num, contador))
if contador == 2:
    print('Esse numero e primo !')
else:
    print('Esse numero não e primo !')