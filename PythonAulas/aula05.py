num1 = float(input('Digite sua nota :'))
num2 = float(input('Digite sua nota :'))
media = (num1 + num2) / 2
print('Sua media foi {:.1f} ' .format(media))
if media >=6.0:
    print('Parabens sua media e azul !')
else:
    print('Va estudar nota vermelha ')