ano = int(input('Qual seu ano de nascimento? '))
idade = 2024 - ano
if idade <= 9:
    print('Você está na categoria Mirim.')
elif idade <= 14:
    print('Você está na categoria Infantil.')
elif idade <= 19:
    print('Você está na categoria Junior.')
elif idade == 20:
    print('Você está na categoria Sênior.')
else:
    print('Você está na categoria Master.')
