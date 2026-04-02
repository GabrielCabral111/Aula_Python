nome = str(input('Digite um nome : ')).strip()

max = nome.upper()
min = nome.lower()
qtde = len(nome) - nome.count(' ')
primeiroNome = len(nome.split()[0])
## primeiroNome =  nome.find(' ')

print('O nome {} tem {} letras'.format(nome, qtde))
print('O nome {} Maiusculo '.format(max))
print('O nome {} Minusculo '.format(min))
print(primeiroNome)
