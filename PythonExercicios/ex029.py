from time import sleep

viagem = float(input('Qual sera a distancia da viagem KM: '))
if viagem <= 200:
    preco = viagem * 0.50
else:
    preco = viagem * 0.45
print('Calculando preço ...')
sleep(3)
print('O preço da viagem e R$:{} '.format(preco))
