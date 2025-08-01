c = ('\033[0m',        #0 - Sem cores
     '\033[0;30;41m',  #1 - Vermelho
     '\033[0;30;42m',  #2 - Verde
     '\033[0;30;43m',  #3 - Amarelo
     '\033[0;30;44m',  #4 - Azul
     '\033[0;30;45m',  #5 - Roxo
     '\033[0;30;47m'   #6 - Branco
     );      


def ajuda(com):
    titulo(f'Acessando o manual do \'{com}\'', 4)
    help(com)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')


comando = ''
while True:
    titulo('Comando de Ajuda PyHelp', 2)
    comando = str(input('Função ou biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('Até Logo!', 1)
