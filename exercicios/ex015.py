dia = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos km o carro andou? '))
pre = (60 * dia) + (0.15 * km)
print('O valor total a ser pago vai ser R${:.2f}.'.format(pre))
