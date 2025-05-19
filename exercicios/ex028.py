import random

num = int(input('Tente acertar o número que a máquina está pensando de 1 a 5: '))
lista = [1,2,3,4,5]
sort = random.choice(lista)
if num == sort:
    print('Você acertou o número! Parabéns!')
else:
    print('Infelizmente você errou, o número era {}.'.format(sort))
