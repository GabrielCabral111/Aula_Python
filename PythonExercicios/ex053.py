
soma = 0
media = 0
maior = 0
pessoas = ''
cont = 0
for c in range(1, 5):
    print('='*10,'{} Pessoa'.format(c), '='*10)
    nome = str(input('Digite seu nome: ')).strip()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('sexo [M/F]: ')).strip().upper()
    soma += idade
    media = soma / 4
    if sexo != 'M' and sexo != 'F':
        print('Resposta invalida')
    elif sexo == 'M':
        if idade > maior:
            maior = idade
            pessoa = nome
    elif sexo == 'F':
        if idade > 20:
            cont += 1
print('A media de idade do grupo e de {:.2f}'.format(media))
print('O home mais velhor tem {} anos e se chama {} '.format(maior, pessoa))
print('Ao todo são {} Mulhers com mais de 20 anos'.format(cont))