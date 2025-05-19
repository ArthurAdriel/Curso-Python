n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
#Verificando qual é o maior
maior = n1
if  n2 > n1:
    maior = n2
if n3 > n1:
    maior = n3
print('O maior número é o {}.'.format(maior))
#Verificando qual é o menor
menor = n1 
if n2 < n1:
    menor = n2
if n3 < n1:
    menor = n3
print('O menor número é o {}.'.format(menor))    
