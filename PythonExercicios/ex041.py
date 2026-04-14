print('='*30)
print(""" LOJA DO CABRAL """)
print('='*30)
preco = float(input('Preço das compras: R$:'))
print('Formas de PAGAMENTO')
print('='*30)
print('[1] à vista DINHEIRO CHEQUE')
print('[2] à vista CARTÃO')
print('[3] 2x no CARTÃO')
print('[4] 3x ou MAIS NO CARTÃO')
opcao = int(input('Qual a opção :'))
if opcao == 1:
    Desconto = preco - (preco * 0.10)
    print('O valor da sua compra e de R$:{:.2f} '.format(preco))
    print('Seu pagamento e Dinheiro tem desconto vai custar R${:.2f} '.format(Desconto))

elif opcao == 2:
    desconto = preco - (preco * 0.05)
    print('O valor da sua compra e de R$:{:.2f} '.format(preco))
    print('Seu pagamento no Cartão tem desconto vai custar R${:.2f} '.format(desconto))
elif opcao == 3:
    parcela = preco / 2
    print('Sua compra será parcelada em 2x de R${:.2f} '.format(parcela))
elif opcao == 4:
    vezes = int(input('Quantas vezes deseja pagar: '))
    parcela = preco / vezes
    juros = preco + (preco * 0.20)
    print('O valor da sua compra e de R$:{:.2f} '.format(preco))
    print('Suas parcelas foram de {}x de R$:{:.2f} '.format(vezes, parcela))
    print('Seu pagamento de 3x ou mais  tem JUROS vai custar R${:.2f} '.format(juros))
else:
    print('Opção invalida')