km = int(input('Quantos quilometros tem a viagem? '))
if km > 200:
    print('A viagem vai custar R${}.'.format(km * 0.45))
else:
    print('A viagem vai custar R${}.'.format(km * 0.50))
    