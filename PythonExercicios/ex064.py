n = 0
res = 0
while True :
    n = int(input('Qual a tabuada que deseja digitar ? '))
    print('-=-' * 15)
    for c in range(1, 11):
        print(f'{n} x {c} = {n * c} ')
    print('-=-' * 15)
    res = int(input('Deseja continuar? [1] para sim e [- 1] Parar '))
    print('-=-' * 15)
    if res < 0 :
        break

print('Programa "Taboada" ENCERRADO.....')
