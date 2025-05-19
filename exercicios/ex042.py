n1 = int(input('Digite um lado do triângulo: '))
n2 = int(input('Digite outro lado do triângulo: '))
n3 = int(input('Digite o último lado do triângulo: '))
if n1 == n2 and n2 == n3:
    print('É um triângulo equilátero.')
elif n1 == n2 or n1 == n3 or n2 == n3:
    print('É um triângulo isósceles.')
else:
    print('É um triângulo escaleno.')
