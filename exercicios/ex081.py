lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Quer continuar? [S/N]: ')).upper().capitalize()[0]
    if sair == 'N':
        break
lista.sort(reverse = True)
print('-=' * 30)
print(f'Você digitou {len(lista)} elementos.')
print(f'A lista em ordem decrescente é {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 não faz parte da lista.')
