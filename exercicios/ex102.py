def fatorial(num, show=False):
    """Calcula o Fatorial de um número.

    Args:
        num (_type_): O número a ser calculado
        show (bool, optional): Mostrar ou não a conta.

    Returns:
        _type_: O valor fatorial do número.
    """
    resp = 1
    for c in range(num, 0, -1):
        if show == True:
            print(c, end='')
            if c > 1:
                print(' X ', end='')
            else:
                print(' = ', end='')
        resp = resp * c
    return resp
print(fatorial(5, show=True))
