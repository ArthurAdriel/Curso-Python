def notas(* numeros, sit=False):
    """Função para analisar notas e situações de alunos.

    Args:
        sit (bool, optional): Valor opcional, indicando se deve ou não adicionar a situação. Defaults to False.
        numeros (_type_): uma ou mais notas dos alunos (aceita várias)

    Returns:
        _type_: Dicionário com várias informações sobre a situação dos alunos 
    """
    lista = {}
    maior = 0
    menor = 0
    total = 0
    media = 0

    for i, n in enumerate(numeros):
        total += n
        if i == 0:
            maior = n
            menor = n
        else:
            if n > maior:
                maior = n
            if n < menor:
                menor = n
    media = total / len(numeros)
    lista['Total'] = len(numeros)
    lista['Maior'] = maior
    lista['Menor'] = menor
    lista['Média'] = media
    if sit:
        if media >= 7:
            lista['Situação'] = 'Boa!'
        if media < 7 and media >= 5:
            lista['Situação'] = 'Razoável!'
        if media < 5:
            lista['Situação'] = 'Ruim!'
    return lista


resp = notas(5.5, 1, 5, sit=True)
print(resp)