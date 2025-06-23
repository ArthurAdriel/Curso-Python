lista = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).upper().capitalize()[0]
    if resp == 'N':
        break
print('-=' * 30)
print(f"{'N°':<4}{'Nome':<10}{'Media':>8}")
print('-' * 26)
for i, a in enumerate(lista):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8}')
while True:
    print('-=' * 30)
    aluno = int(input('Qual aluno você quer ver? Escreva o número dele: '))
    print(f'As notas de {lista[aluno][0]} são {lista[aluno][1]}')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).upper().capitalize()[0]
    if resp == 'N':
        break
print('Fechando o Programa...')
    