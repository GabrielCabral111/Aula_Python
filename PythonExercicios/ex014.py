qdia = int(input('Quantos dias voce quer alugar: '))
qkm = float(input('Quantos km rodados: '))
totalDia = 60 * qdia
totalKm =  0.15 * qkm
totalPagar = totalDia + totalKm
print('Você alugou o carro por {} Dias e andou {} KM entao irar pagar R$: {:.2f}'.format(qdia, qkm, totalPagar))