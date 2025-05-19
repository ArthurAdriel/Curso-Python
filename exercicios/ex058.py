import random

num = int(input('Tente acertar o número que a máquina está pensando de 1 a 5: '))
lista = [1,2,3,4,5]
cont = 0
acertou = "False"
while acertou != "True":
    sort = random.choice(lista)
    cont = cont + 1
    if num == sort:
        print('Você acertou o número com {} tentativas! Parabéns! '.format(cont))
        acertou = "True"
    else:
        num = int(input("Você errou! Tente novamente: "))
