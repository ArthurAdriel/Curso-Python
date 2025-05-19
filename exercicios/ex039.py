ano = int(input('Qual o seu ano de nascimento? '))
idade = 2024 - ano
if idade < 18:
    print('Você ainda não precisa de se alistar, vai se alistar apenas daqui {} anos.'.format(18 - idade))
elif idade == 18:
    print('Você está no ano de se alistar! ')
else:
    print('Você já passou da idade de se alistar, já passou {} anos de quando você deveria ter se alistado.'.format(idade - 18))

