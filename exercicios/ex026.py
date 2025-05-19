frase = str(input('Escreva uma frase: ')).lower().strip()
print('A letra A aparece {} vezes na frase.'.format(frase.count('a')))
print('A primeira vez que aparece a letra A é na posição {}.'.format(frase.find('a') +1))
print('A ultima vez que aparece a letra A é na posição {}.'.format(frase.rfind('a') +1))
