preco = float(input('Qual o preço do produto? R$ '))
desconto = preco - (preco * 0.05)
print('O produto que custa R$:{} com 5% de desconto fica {:.2f} ' . format(preco, desconto))