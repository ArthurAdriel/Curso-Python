lista = [[ ],[ ]]
for n in range(0, 7):
    numero = int(input(f'Digite o {n + 1}° valor: '))
    if numero % 2 == 0:
        lista[0].append(numero)
    else:
        lista[1].append(numero)
print('-=' * 30)
print(f'Os valores pares digitados foram {lista[0]}')
print(f'Os valores ímpares digitados foram {lista[1]}')
