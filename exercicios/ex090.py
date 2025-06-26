aluno = {}
aluno['Nome'] = str(input('Nome: '))
aluno['Media'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno['Media'] >= 7:
    aluno['Situação'] = 'aprovado'
else:
    aluno['Situação'] = 'reprovado'
for k, v in aluno.items():
    print(f'{k} é igual a {v}.')
