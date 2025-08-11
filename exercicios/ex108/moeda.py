def metade(n = 0):
    return n / 2


def dobro(n = 0):
    return n * 2


def aumentar(n = 0, p = 0):
    porcentagem = p / 100
    r = n * porcentagem
    return n + r


def diminuir(n = 0, p = 0):
    porcentagem = p / 100
    r = n * porcentagem
    return n - r


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:>.2f}'.replace('.', ',')
