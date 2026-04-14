print('='*30)
print(""" Calculo de IMC """)
print('='*30)
peso = float(input('Qual e os seu peso (KM)?'))
altura = float(input('Qual e a sua altura (m)?'))
imc = peso / (altura ** 2)
print('Seu IMC e de {} '.format(imc))
if imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc <= 25:
    print('Peso ideal')
elif imc >= 25 and imc <= 30:
    print('Sobrepeso')
elif imc >= 30 and imc <= 40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')