nome = str(input('Qual O seu nome :'))
if nome == 'Gabriel':
    print('Que nome bonito')
elif nome == 'Pedro' or nome == 'Maria'or nome == 'Gabriela':
    print('nome popular ')
elif nome in 'ana fabiana leticia paula':
    print('nome Normal !')
else:
    print('seu nome ate que e legal')
print('Tenha um bom dia {}'.format(nome))