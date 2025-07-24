from time import sleep

def contador(inicio, fim, passo):
    print('-=' * 30)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    
    if passo < 0:
        passo = passo * -1
    if passo == 0:
        passo = 1
    if inicio < fim:
        while inicio <= fim:
            print(f'{inicio}', end=' ', flush=True)
            sleep(0.5)
            inicio = inicio + passo
    else:
        while fim <= inicio:
            print(f'{inicio}', end=' ', flush=True)
            sleep(0.5)
            inicio = inicio - passo
    print()
    print('-=' * 30)

contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é a sua vez de personalizar a contagem! ')
i = int(input('Início: '))
f = int(input('Fim : '))
p = int(input('Passo: '))
contador(i, f, p)
