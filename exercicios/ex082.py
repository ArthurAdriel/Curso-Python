listaCompleta = []
pares = []
impares = []
while True:
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        pares.append(numero)
        listaCompleta.append(numero)
    else:
        impares.append(numero)
        listaCompleta.append(numero)
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Quer continuar? [S/N]: ')).upper().capitalize()[0]
    if sair == 'N':
        break
listaCompleta.sort()
pares.sort()
impares.sort()
print('-=' * 30)
print(f'A lista completa é {listaCompleta}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
