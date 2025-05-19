import random
lista = [1, 2, 3, 4, 5, 6, 7, 8, 10]
cont = 0

print("-=" * 15)
print("VAMOS JOGAR PAR OU ÍMPAR")
print("-=" * 15)

while True:
    num = int(input("Digite um valor: "))
    esc = str(input("Você quer par ou ímpar? [P/I] ")).strip().upper()
    sort = random.choice(lista)
    total = num + sort

    if total % 2 == 0:
        ganhador = "P"
        print("-" * 30)
        print(f"Você jogou {num} e a máquina jogou {sort}, total de {total}. DEU PAR!")
        print("-" * 30)
    else:
        ganhador = "I"
        print("-" * 30)
        print(f"Você jogou {num} e a máquina jogou {sort}, total de {total}. DEU ÍMPAR!")
        print("-" * 30)
    
    if esc == ganhador:
        print("VOCÊ VENCEU!!!")
        print("Vamos jogar novamente... ")
        print("-=" * 15)
        cont += 1
    else:
        print("VOCÊ PERDEU!")
        break
print(f"Você ganhou da máquina {cont} vezes!")
