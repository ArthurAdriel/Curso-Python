def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {a:.2f}m².')


print('-' * 22)
print(' Controle de Terrenos')
print('-' * 22)
l = float(input('Largura (M): '))
c = float(input('Comprimento (M):'))
area(l, c)
