s = cont = 0
while True:
    num = int(input("Digite um valor? [999 para parar] "))
    if num == 999:
        break
    cont += 1
    s += num
print(f"A soma dos {cont} números é de {s}!")
