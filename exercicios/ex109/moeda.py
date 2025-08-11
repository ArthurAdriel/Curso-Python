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
