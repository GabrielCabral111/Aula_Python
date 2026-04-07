salario = float(input(' Qual e o seu salario atual :'))
if salario <=1550 :
    novo_salario = salario + (salario * 0.15)
else:
    novo_salario = salario + (salario * 0.05)
print('Seu salario de R$:{:.2f} agora e R$:{:.2f} ' .format(salario, novo_salario))