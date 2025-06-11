listaNum = []
while True:
    numero = int(input('Digite um valor: '))
    if numero in listaNum:
        print('Valor duplicado! Não vou adicionar...')
    else:
        listaNum.append(numero)
        print('Número adicionado com sucesso!')
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Quer continuar: [S/N]: ')).upper().capitalize()[0]
    if sair == 'N':
        break
listaNum.sort()
print(f'Você digitou os valores {listaNum}')
