var = input('Digite algo: ')
cores = {
    'limpa' : '\033[m',
    'branco' : '\033[30m',
    'vermelho' : '\033[31m',
    'verde' : '\033[32m',
    'amarelo' : '\033[33m',
    'azul' : '\033[34m',
    'roxo' : '\033[35m',
    'azulbebe' : '\033[36m'
}
print('O tipo primitivo é {}{}{}.'.format(cores['branco'],type(var),cores['limpa']))
print('Tem espaços? {}{}{}'.format(cores['amarelo'],var.isspace(),cores['limpa']))
print('É alfabético? {}{}{}'.format(cores['azul'],var.isalpha(),cores['limpa']))
print('É alfanumérico? {}{}{}'.format(cores['azulbebe'],var.isalnum(),cores['limpa']))
print('Só tem letra maiúscula? {}{}{}'.format(cores['roxo'],var.isupper(),cores['limpa']))
print('Só tem letra minúscula? {}{}{}'.format(cores['verde'],var.islower(),cores['limpa']))
print('Está capitalizada? {}{}{}'.format(cores['vermelho'],var.istitle(),cores['limpa']))
