grupo = []
jogador = {}
gols = []
while True:
    jogador.clear()
    gols.clear()
    jogador['Nome'] = str(input('Nome: '))
    partidas = int(input(f'Quantas partidas o {jogador["Nome"]} jogou? '))
    for c in range(0, partidas):
        gols.append(int(input(f'Quantos gols na partida {c + 1}? ')))
    jogador['Gols'] = gols.copy()
    jogador['Total'] = sum(gols)
    grupo.append(jogador.copy())
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().capitalize()[0]
    print('-' * 30)
    if resp == 'N':
        break
print('-=' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, p in enumerate(grupo):
    print(f'{k:>3}', end=' ')
    for d in p.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    codigo = int(input('Você quer mostrar os dados de qual jogador? (999 Encerra) '))
    if codigo == 999:
        break
    if codigo >= len(grupo):
        print('ERRO! Jogador não existe! ')
    else:
        print(f'-- Levantamento do Jogador {grupo[codigo]["Nome"]}')
        for c, g in enumerate(grupo[codigo]['Gols']):
            print(f'Na partida {c + 1} fez {g} gols.')
    print('-' * 40)
print('<< Volte Sempre >>')
