import random
from time import sleep
jogos = []
print('-' * 30)
print(f"{'JOGA NA MEGA SENA':^30}")
print('-' * 30)
quantidade = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'-=-=-= SORTEANDO {quantidade} JOGOS -=-=-=')
for j in range(0, quantidade):
    jogo = []
    for c in range(0, 6):
        numero = random.randint(1, 60)
        while True:
            if numero in jogo:
                numero = random.randint(1, 60)
            else:
                break
        jogo.append(numero)
        jogo.sort()
    jogos.append(jogo)
for c in range(0, quantidade):
    print(f'Jogo {c + 1}: {jogos[c]}')
    sleep(1)
print('-=' *  5, f' Boa Sorte!! ', '-=' * 5)
