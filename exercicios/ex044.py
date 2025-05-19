print('\033[30m=\033[m' *20 )
print('\033[31mLoja do Galo\033[m')
print('\033[30m=\033[m' *20 )
pre = float(input('Qual o preço de produto? R$'))
cond = str(input('Qual será a forma de pagamento? ')).lower()
if cond == 'dinheiro' and 'débito':
    print('Você vai ter 10% de desconto! O valor vai ficar R${}. '.format(pre - (pre * 0.10)))
elif cond == 'crédito':
    print('Você vai ter 5% de desconto! O valor vai ficar R${}. '.format(pre - (pre * 0.05)))
elif cond == 'crédito 2x':
    print('Você não vai ter juros para dividir em duas vezes! E o valor vai ser R${}.'.format(pre))
elif cond == "crédito 3x" and "crédito 4x" and "crédito 5x" and "crédito 6x" and "crédito 7x":
    print('Você vai ter um juros de 20%. O valor vai ficar em R${}. '.format(pre + (pre * 0.20)))
else:
    print('Não aceitamos essa forma de pagamento. Ou você escreveu errado.')
    