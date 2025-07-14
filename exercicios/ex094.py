grupo = list()
pessoa = dict()
total = 0
acimamedia = []
while True:
    pessoa['Nome'] = str(input('Nome: '))
    pessoa['Sexo'] = str(input('Sexo: [F/M] ')).upper().capitalize()[0]
    pessoa['Idade'] = int(input('Idade: '))
    total = total + pessoa['Idade']
    grupo.append(pessoa.copy())
    pessoa.clear()
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().capitalize()[0]
    if resp == 'N':
        break
media = total / len(grupo)
print('-=' * 30)
print(f'A) O grupo tem {len(grupo)} pessoas. ')
print(f'B) A média de idade é de {media:5.2f} anos.')
print('C) As mulheres cadastradas foram: ', end='')
for p in grupo:
    if p['Sexo'] in 'F':
        print(f'{p["Nome"]}',end='.')
print()
print(f'D) Lista das pessoas que estão acima da média:', end='')
for p in grupo:
    if p['Idade'] >= media:
        print(f'{p["Nome"]}',end='.')
print()
print('<< Encerrado >>')
