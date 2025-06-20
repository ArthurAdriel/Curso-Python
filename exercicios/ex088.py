import random
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
        jogo.append(numero)
    jogos.append(jogo)
for c in range(0, quantidade):
    print(f'Jogo {c + 1}: {jogos[c]}')
print('-=-=-= BOA SORTE -=-=-=')
