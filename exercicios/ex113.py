def leiaInt():
    while True:
        try:
            n = int(input('Digite um número inteiro: '))
            return n  
        except KeyboardInterrupt:
            print('\033[0;31mO usuário preferiu não informar os dados.\033[m')
            return 0
        except:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
            continue

def leiaFloat():
    while True:
        try:
            n = float(input('Digite um número real: '))
            return n  
        except KeyboardInterrupt:
            print('\033[0;31mO usuário preferiu não informar os dados.\033[m')
            return 0
        except:
            print('\033[0;31mERRO! Digite um número real válido.\033[m')
    
numInteiro = leiaInt()
numReal = leiaFloat()
print(f'Você acabou de digitar o número {numInteiro}. ')
print(f'Você acabou de digitar o número {numReal}. ')
