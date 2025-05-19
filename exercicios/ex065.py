cont = maior = total = media = 0
menor = 0
sair = ""
while sair != "N":
    num = int(input("Digite um número: "))
    sair = str(input("Quer continuar? [S/N]")).upper().strip()
    cont += 1
    total += num
    if cont == 1:
        menor = num
        maior = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
media = total / cont
print("Você digitou {} números e a média foi de {}!".format(cont, media))
print("O maior valor foi de {} e o menor foi de {}.".format(maior, menor))
    