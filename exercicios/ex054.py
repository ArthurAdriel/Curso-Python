from datetime import date
atual = date.today().year
cont_maior = 0
cont_menor = 0
for c in range(1, 8):
    nasc = int(input('Qual ano eesa pessoa nasceu? '))
    idade = atual - nasc
    if idade < 21:
        cont_menor += 1
    else:
        cont_maior += 1
print('Dessas 7 pessoas {} são maiores de idade e {} são menores de idade. '.format(cont_maior, cont_menor))
