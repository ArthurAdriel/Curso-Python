alternativa = 0
n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
while alternativa != 5:
    print("[ 1 ] Somar")
    print("[ 2 ] Multiplicar")
    print("[ 3 ] Maior")
    print("[ 4 ] Novos números")
    print("[ 5 ] Sair do programa")
    alternativa = int(input(">>>> Qual a sua opção? "))
    if alternativa == 1:
        print("A soma dos números é {}.".format(n1 + n2))
    elif alternativa == 2:
        print("A multiplicação dos números é {}".format(n1 * n2))
    elif alternativa == 3:
        if n1 > n2:
            print("O número maior é o {}!".format(n1))
        else:
            print("O número maior é o {}".format(n2))
    elif alternativa == 4:
        n1 = int(input("Primeiro valor: "))
        n2 = int(input("Segundo valor: "))
print("Você usou o programa com sucesso!")