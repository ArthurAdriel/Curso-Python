while True:
    print("-" * 38)
    num = int(input("Você quer ver a tabuada de qual valor? "))
    print("-" * 38)
    if num < 0:
        break
    for c in range (1, 11, 1):
        print(f"{c} X {num} = {c * num}")
print("PROGRAMA TABUADA ENCERRADO. Volte sempre!")
