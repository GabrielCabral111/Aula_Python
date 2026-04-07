velocidade = float(input('Qual a velocidade do carro ?'))
if velocidade > 80:
    print('velocidade a cima do limite !!')
    multa = (velocidade - 80) * 7
    print('Você foi multado !!')
    print('terar que pagar R$:{}'.format(multa))
print('Velocidade permitida -W- ')