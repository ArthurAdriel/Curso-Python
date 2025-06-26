import random
jogadores = list()
jogador = dict()
print('Valores sorteados: ')
for c in range(0, 4):
    jogador['numero'] = c + 1
    jogador['dado'] = random.randint(1, 6)
    jogadores.append(jogador.copy())
for jogador in jogadores:
    print(f'O jogador{jogador["numero"]} tirou {jogador["dado"]}')    
