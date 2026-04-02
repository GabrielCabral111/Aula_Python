num = int(input('Digite um numeo de 9 a 9999 : '))

uni = num // 1 % 10
dec = num // 10 % 10
cen = num // 100 % 10
milh = num // 1000 % 10

print('Unidade : {}'.format(uni))
print('Dezena : {}'.format(dec))
print('Centena : {}'.format(cen))
print('Milha : {}'.format(milh))