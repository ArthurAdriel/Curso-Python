num = int(input('Escreva um número: '))
conv = str(input('Você quer converter para binário, octal ou hexadecimal? ')).lower()
if conv == 'binário':
    print('O seu número em binário é {}.'.format(bin(num)[2:]))
elif conv == 'octal':
    print('O seu número em octal é {}.'.format(oct(num)[2:]))
elif conv == 'hexadecimal':
    print('O seu número em hexadecimal é {}.'.format(hex(num)[2:]))
else:
    print('Você digitou errado a palavra.')
