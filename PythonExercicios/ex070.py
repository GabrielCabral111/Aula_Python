times = (
    'Palmeiras',
    'Flamengo',
    'Fluminense',
    'São Paulo',
    'Athletico-PR',
    'Bahia',
    'RB Bragantino',
    'Coritiba',
    'Grêmio',
    'Vasco',
    'Vitória',
    'Corinthians',
    'Internacional',
    'Atlético-MG',
    'Chapecoense',
    'Santos',
    'Botafogo',
    'Mirassol',
    'Remo',
    'Cruzeiro'
)
print('-=-'*30)
print('{:^20}'.format(' Campionato Brasileiro '))
print('-=-'*30)
print(f'Lista dos times do Brasileirao: {times}')
print('-'*30)
print(f'Os primeiros 5 times sao {times[0:6]}')
print('-'*30)
print(f'Os ultimos 4 times sao {times[-4:-1]}')
print('-'*30)
print(f'em ordem alfabetica {sorted(times)}')
print('-'*30)
print(f'A chapecoense esta na posiçâo {times.index("Chapecoense")+1}')
