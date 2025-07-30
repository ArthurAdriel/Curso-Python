def ficha(n='<Desconhecido>', g=0):
    print(f'O jogador {n} fez {g} gol(s) no campeonato. ')


print('-' * 30)
nome = str(input('Nome do Jogador: '))
gols = str(input('Quantos Gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(g=gols)
else:
    ficha(nome, gols)
print('-' * 30)
