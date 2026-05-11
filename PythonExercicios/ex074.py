palavra = ('Aprender', 'Programara', 'Linguagem', 'Python','Curso','Gratis','Estudar','Praticar','Trabalhar','Mercado','Programador','Futuro' )

for p in palavra:
    print(f'\nNa palavra {p} temos', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')

