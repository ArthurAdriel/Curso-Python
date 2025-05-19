maior = 0 
menor = 0
for c in range(1, 6):
    peso = float(input('Qual o peso da {}° pessoa? '.format(c)))
    if c == 1:
        maior = peso 
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O pessoa com o maior peso, pesa {}kg. A com menor peso, pesa {}kg.'.format(maior, menor))