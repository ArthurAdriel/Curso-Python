print('='*20)
print('EMPRÉSTIMO DE BANCO')
print('='*20)
casa = int(input('Qual o valor da casa? R$'))
sal = float(input('Qual o seu salário? R$'))
ano = int(input('Com quantos anos você quer quitar a casa?'))
prest = casa / (ano * 12)
if prest > (sal * 0.30):
    print('Seu empréstimo foi recusado, pois seu salário é baixo. ')
else:
    print('A parcela que você vai ter que pagar por mês é R${:.2f}.'.format(prest))
