num = total = cont = 0
num = int(input("Digite um número: [999 para parar] "))
while num != 999:
    total += num
    cont += 1
    num = int(input("Digite um número: [999 para parar] "))
print("Você digitou {} números, e a soma de todos os números é {}.".format(cont, total))
