print('{:=^40}'.format(' 10 TERMOS DE UMA PA '))

num = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

contador = 1
termo = num

while contador <= 10:
    print('{}'.format(termo), end=' -> ')
    termo += razao
    contador += 1

print('FIM')