print('-' * 20)
print('{:^20}'.format(' Loja do Cabral '))
print('-' * 20)
cont = totalProdutos = caro = pBarato = 0
nBarato = ''
while True:
    print('-' * 20)
    print('{} {:^20}'.format(cont, ' Produtos Comprados'))
    print('-' * 20)
    Produto = str(input('Qual o nome do produto: '))
    preco = int(input('Preço:'))
    print('-' * 20)
    cont += 1
    totalProdutos += preco
    if preco > 1000:
        caro += 1
    if cont == 1:
        nBarato = Produto
        pBarato = preco
    else:

        if preco < pBarato:
            pBarato = preco
            nBarato = Produto
    res = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while res not in 'SN':
        res = str(input('Resposta invalida! | Deseja continuar [S/N] ')).upper().strip()[0]
    if res == 'N':
        break
print('{:=^30}'.format(' Fim Do Programa .... '))
print(f'Você comprou {cont} Prdutos')
print(f'O total da compra foi de R$: {totalProdutos}')
print(f'Temos {caro} Produtos que custam mais de R$:1000')
print(f'O produto mais barato foi {nBarato} que custa R$: {pBarato:.2f}')