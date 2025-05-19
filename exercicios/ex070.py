total = prod1000 = menor = cont = 0
barato = " "
print("-" * 34)
print("        LOJA SUPER BARATÃO        ")
print("-" * 34)
while True:
    nome = str(input("Nome do produto: ")).strip().capitalize()
    preco = int(input("Preço: R$"))
    total += preco
    cont += 1
    if preco >= 1000:
        prod1000 += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = nome 
    sair = " "
    while sair not in "SN":
        sair = str(input("Quer continuar? [S/N]")).upper().strip()[0]
    if sair == "N":
        break
print(f"O total da compra foi de R${total}.")
print(f"Temos {prod1000} produtos custando mais de R$1000,00.")
print(f"O produto mais barato foi {barato} que custa R${menor}.")
