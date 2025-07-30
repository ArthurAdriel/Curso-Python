def leiaInt(n):
    while True:
        if n.isnumeric():
            break
        else:
            print('-' * 40)
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
            n = input('Digite um número: ')
    return n


print('-' * 40)
n = leiaInt(input('Digite um número: '))
print(f'Você acabou de digitar o número {n}. ')
print('-' * 40)
