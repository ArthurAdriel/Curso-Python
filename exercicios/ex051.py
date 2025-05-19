pt = int(input('Qual o primeiro termo? '))
razao = int(input('Qual a razão? '))
decimo = pt + (10 - 1) * razao
for c in range (pt, decimo + razao, razao):
    print('{} '.format(c), end='> ')
print('ACABOU')
