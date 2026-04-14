
print('Escolha um numero de 1 a 3 ')
print('- 1 para Binario')
print('- 2 para Octal')
print('- 3 para Hexadecimal')
resul = int(input('Escolha o numero de: '))
num = int(input('Digite um numero :'))
if resul == 1:
    print('O numero digitado e {} e a forma dele de Binario é {} :'.format(num ,bin(num)[2:]))
elif resul == 2:
    print('O numero digitado e {} e a forma dele de Octal é {} :'.format(num ,oct(num)[2:]))
elif resul == 3:
    print('O numero digitado e {} e a forma dele de Hexadecimal é {} :'.format(num ,hex(num)[2:]))

else:
    print('Digito errado escolha o numeor 1 , 2 ou 3')