num = int(input("Digite um número: "))
multiplicacao = num
multiplicador = num
while multiplicador > 1:
    multiplicador = multiplicador -1
    multiplicacao = multiplicacao * multiplicador
    print(multiplicador)
print("O número fatorial de {} é {}!".format(num, multiplicacao))
