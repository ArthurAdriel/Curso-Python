velo = float(input('Qual a velocidade que o carro estava? '))
if velo >= 80:
    mul = velo - 80
    print('O carro estava a cima do limite de velocidade, por isso tomou uma multa de R${}.'.format(mul * 7))
else:    
    print('O carro estava dentro do limite da rodovia.')    