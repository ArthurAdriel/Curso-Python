from datetime import date 

def voto(a):
    global idade
    ano = date.today().year
    idade = ano - a

    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA'
    elif idade > 15 and idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'


print('-' * 25)
nascimento = int(input('Em que ano você nasceu? '))
resp = voto(nascimento)
print(f'Com {idade} anos: {resp}')
print('-' * 25)
