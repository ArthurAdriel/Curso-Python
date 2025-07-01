from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6), 
        'jogador4': randint(1, 6)}
ranking = list()
print('-=' * 30)
print('Valores sorteados!')
for k, v in jogo.items():
    print(f'    O {k} tirou {v}')
    sleep(0.5)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
print('Em ordem! ')
for i, n in enumerate(ranking):
    print(f'    {i + 1}° Lugar: {n[0]} tirou {n[1]}')
    sleep(0.5)
print('-=' * 30)