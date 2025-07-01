pessoa = {}
pessoa['Nome'] = str(input('Nome: '))
pessoa['Ano'] = int(input('Ano de Nascimento: '))
pessoa['Ctps'] = int(input('Carteira de Trabalho: (0 não tem): '))
if pessoa['Ctps'] != 0:
    pessoa['Contratacao'] = int(input('Ano de Contratação: '))
    pessoa['Salario'] = float(input('Salário: '))
    pessoa['Aposentadoria'] = pessoa['Contratacao'] + 35
print('-=' * 30)
print(pessoa)
for k, v in pessoa.items():
    print(f'{k} tem o valor {v}')
