largura = float(input('Qual a largura da parede? '))
altura = float(input('Qual a altura da parede? '))
area = largura * altura
tinta = area / 2

print('Sua parede tem a dimensão de {} x {} e a area e de {}m .'.format(largura, altura, area))
print('Para pintar essa parede você precisarã de {:.2f} de tinta' .format(tinta))