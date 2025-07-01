jogador = {}
gols = []
jogador['Nome'] = str(input('Nome: '))
partidas = int(input(f'Quantas partidas o {jogador["Nome"]} jogou? '))
for c in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {c}? ')))
jogador['Gols'] = gols
jogador['Total'] = sum(gols)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)
print(f'O jogador {jogador["Nome"]} jogou {partidas} partidas.')
for c in range(0, partidas):
    print(f'    => Na partida {c}, fez {jogador["Gols"][c]} gols.')
print(f'Foi um total de {jogador["Total"]} gols.')
