
n = str(input('Digite seu nome completo: ')).strip()

nome = n.split()

print('Ola {} e um prazer te conhecer ' .format(nome[0]))
print('Seu ultimo nome e {} ' .format(nome[len(nome)-1]))