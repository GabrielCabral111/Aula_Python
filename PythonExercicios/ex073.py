produtos = (
    'Arroz', 25.90,
    'Feijão', 8.50,
    'Macarrão', 6.99,
    'Leite', 5.49,
    'Café', 18.75,
    'Açúcar', 4.20,
    'Óleo', 7.80,
    'Pão', 12.00,
    'Manteiga', 9.99,
    'Queijo', 15.50
)
print('-'*35)
print('{:^35}'.format(' LISTA DE PRODUTOS '))
print('-'*35)
for produto in range(0, len(produtos)):
    if produto % 2 == 0:
        print(f'{produtos[produto]:.<20} ', end='' )
    else:
        print(f'R$:{produtos[produto]:>5.2f}')
print('-'*35)
