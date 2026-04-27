from datetime import date
novos = 0
velhos = 0
ano = date.today().year
for c in range(1, 8):
    nascimento = int(input('Em que ano a {} pessoa nasceu: ' .format(c)))
    idade = ano - nascimento
    if idade >= 18:
        novos += 1
    else:
        velhos += 1
print('Ao todo tivemos {} pessoas maiores de idade' .format(novos))
print('E também tivemos {} pessoas menores de idade' .format(velhos))
