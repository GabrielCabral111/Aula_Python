print('-' * 20)
print('{:^20}'.format(' Cadastro de pessoas '))
idade = 0
cont = 0
maiorDeIdade = 0
totalM = 0
menorF = 0
while True:
    print('-' * 20)
    print('{} {:^20}'.format(cont ,' Pessoas Cadastradas  '))
    print('-' * 20)
    idade = int(input('idade: '))
    sexo = str(input('sexo: [M/F] ')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Sexo não cadastrado. Digite qual e o seu Sexo:  [M/F] ')).strip().upper()[0]
    if idade >= 18:
        maiorDeIdade += 1
    if sexo == 'M':
        totalM += 1
    if sexo == 'F' and idade < 20:
        menorF += 1
    print('-' * 20)
    cadastro = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while cadastro not in 'SN':
        cadastro = str(input('Resposta invalida! | Deseja continuar [S/N] ')).strip().upper()[0]
    cont += 1
    if cadastro == 'N':
        break

print('{:=^30}'.format(' Fim Do Programa .... '))
print(f'Você cadastou {cont} pessoas')
print(f'{maiorDeIdade} pessoas são maiores de Idade')
print(f'Foram cadastradas {totalM} Homens')
print(f'Foram cadastradas {menorF} Mulheres que tem menos de 20 anos')



