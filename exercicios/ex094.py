grupo = list()
pessoa = dict()
total = 0
acimamedia = []
mulheres = []
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
print(f'- O grupo tem {len(grupo)} pessoas. ')
print(f'A média de idade é de {media} anos.')
print('As mulheres cadastradas foram: ', end='')
for p in grupo:
    for k, v in p.items():
        if k == 'Sexo' and v == 'F':
            mulheres.append(p)
        if k == 'Idade' and v > media:
            acimamedia.append(p)
for n in mulheres:
    for k, v in n.items():
        if k == 'Nome':
            print(v, end='. ')
print()
print(f'Lista das pessoas que estão acima da média:')
for c in acimamedia:
    print(c)
    print()
print('<< Encerrado >>')
