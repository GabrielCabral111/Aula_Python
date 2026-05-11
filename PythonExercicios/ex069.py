ex = ('zero', 'um', 'dois', 'trez', 'quatro' , 'cinco', 'seis', 'sete', 'oito', 'nove', 'des', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis','dezesete', 'dezoito', 'dezenove', 'vinte')
numero = int(input('Digite um numero de 0 a 20:'))
while numero > 20 or numero < 0:
    numero = int(input('numero errado!! Digite um numero de 0 a 20:'))
print(f'O numero digitado foi {ex[numero]}')


