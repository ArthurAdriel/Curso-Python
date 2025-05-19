sal = float(input('Digite o salário: R$'))
if sal > 1250:
    sal = sal + sal * 0.10
else:
    sal = sal + sal * 0.15
print('O novo salário é de R${:.2f}.'.format(sal))
