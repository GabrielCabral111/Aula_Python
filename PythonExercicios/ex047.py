soma = 0
impar = []
for c in range(1,7 ):
    num = int(input('Digite um numero :'))
    if num % 2 == 0:
        soma += num
    else:
        impar.append(num)
print('O total da soma e {} e {} Impar ' .format(soma,impar))