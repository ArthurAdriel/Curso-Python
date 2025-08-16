def metade(n = 0, formatado = True):
    n = n / 2
    if formatado == True:
        n = moeda(n)
    return n 


def dobro(n = 0, formatado = True):
    n = n * 2
    if formatado == True:
        n = moeda(n)
    return n 


def aumentar(n = 0, p = 0, formatado = True):
    porcentagem = p / 100
    r = n * porcentagem
    resp = n + r
    if formatado == True:
        resp = moeda(resp)
    return resp


def diminuir(n = 0, p = 0, formatado = True):
    porcentagem = p / 100
    r = n * porcentagem
    resp = n - r
    if formatado == True:
        resp = moeda(resp)
    return resp


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:>.2f}'.replace('.', ',')


def resumo(n, a=0, d=0):
    print('-' * 30)
    print(f'{"Resumo do Valor":^30}')
    print('-' * 30)
    print(f'"Preço analisado:" \t{moeda(n)}')
    print(f'"Dobro do Preço" \t{dobro(n)}')
    print(f'"Metade do Preço" \t{metade(n)}')
    print(f'{a}"80% de Aumento" \t{aumentar(n, a)}')
    print(f'{d}"% de Redução " \t{diminuir(n, d)}')
    print('-' * 30)
