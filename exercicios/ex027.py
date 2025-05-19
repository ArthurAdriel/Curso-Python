nome = str(input('Qual o seu nome? '))
div = nome.split()
print('O seu primeiro nome é {}, e o último é {}.'.format(div[0], div[len(div) -1]))
