frase = str(input('Escreva uma frase: ')).strip().upper()
palavras = frase.split()
junto = ' '.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)
if junto == inverso:
    print('Sua frase é um palíndromo!')
else:
    print('Sua frase não é um palíndromo!')