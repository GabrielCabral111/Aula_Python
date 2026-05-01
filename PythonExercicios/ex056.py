from time import sleep

resposta = 0
soma = 0
mult = 0

num1 = int(input('Digite o primeiro  numero : '))
num2 = int(input('Digite o segundo numero : '))
while resposta != 5:
    print('[1] somar ')
    print('[2] Multiplicar ')
    print('[3] Maior ')
    print('[4] Novos numeros ')
    print('[5] Sair do programa ')
    resposta = int(input('>>>>> Qual a sua opcao : '))
    if resposta == 1:
        soma = num1 + num2
        print('A soma entre {} e {} foi {}'.format(num1,num2,soma))
        print('-=' * 10)
    elif resposta == 2:
        mult = num1 * num2
        print('A Multiplicao entre {} e {} foi {}'.format(num1,num2,mult))
        print('-=' * 10)
    elif resposta == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print('Entre {} e {} o numero maior e {} '.format(num1,num2,maior))
        print('-='*10)
    elif resposta == 4:
        num1 = int(input('primeiro numero : '))
        num2 = int(input('segundo numero : '))
    elif resposta == 5:
        print('finalizando...')
        print('-=' * 10)
    else:
        print('opcao invalida. tente novamente')
sleep(2)
print('Fim do Programa.... Volte sempre!')

