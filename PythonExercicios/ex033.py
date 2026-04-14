print('='*30)
print("""Aprovaçao de Empréstimo""")
print('='*30)
valor_casa = float(input('Qual o valor da casa? R$:'))
salario = float(input('Qual e o seu salario R$:'))
anos = int(input('Quantos anos deseja pagar: '))
prestacao = valor_casa/(anos * 12)
if prestacao > salario * 0.3:
    print('Empréstimo NEGADO')

else:
    print('Empréstimo APROVADO')
    print('Você vai pagar a casa em {} anos'.format(anos))
    print('A prestação será de R$: {:.2f}'.format(prestacao))