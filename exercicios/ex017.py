import math
catO = float(input('Qual é o cateto oposto? '))
catA = float(input('Qual é o cateto adjascente? '))
hipo = math.hypot(catA, catO)
print('O comprimento da hipotenusa é {:.2f}.'.format(hipo))
