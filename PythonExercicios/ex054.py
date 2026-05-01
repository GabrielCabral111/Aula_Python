resposta = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]
if resposta != 'M' and resposta != 'F':
     while resposta != 'M' and resposta != 'F' :
        resposta = str(input('Dados invalidos. Por favor, informe seu sexo [M/F]: ')).strip().upper()[0]

print('Sexo {} registrado com sucesso!'.format(resposta))