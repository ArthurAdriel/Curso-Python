import random
numeros = []
def sorteio():
    for c in range(0, 5):
        numeros.append(random.randint(1, 20))
    print(f'Sorteando 5 valores da lista: {numeros}')
def somaPar(lista):
    total = 0
    for n in lista:
        if n % 2 == 0:
            total = total + n 
    print(f'Somando os valores pares de {numeros}, a soma deles é de {total}.')


sorteio()
somaPar(numeros)
