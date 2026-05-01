print('{:=^40}'.format(' 10 TERMOS DE UMA PA '))
num = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
contador = 1
termo = num
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while contador <= total:
        print('{}'.format(termo), end=' -> ')
        termo += razao
        contador += 1

    print('\nPausa ...')
    mais = int(input('Quantos termos quer a mais: '))
print('Progressão finalizada .... com {} termos mostrados '.format(total))
