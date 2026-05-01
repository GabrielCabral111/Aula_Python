frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras).strip()
contrario = ''
for letra in range(len(junto)-1,-1,-1):
    contrario += junto[letra]
if frase == contrario:
    print('A palavra {} palindromo'.format(junto))
else:
    print('Não palindromo')
print('palavra {} e ao contrario {}'.format(junto,contrario))


