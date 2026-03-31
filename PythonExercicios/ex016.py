import math

Cat1 = float(input('Digite o valor do comprimento do cateto oposto: '))
cat2 = float(input('Digite o valor do comprimento do cateto adjacente: '))

print('A hipotenusa e {:.2f} '.format(math.hypot(Cat1,cat2)))
