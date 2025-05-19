print("-" * 23)
print("Sequência de Fibonacci")
print("-" * 23)
term = int(input("Quantos termos você quer ver? "))
pt = 0
st = 1
print("{} > {} > ". format(pt, st), end="")
while (term - 1) > 0:
    soma = pt + st
    term = term - 1
    print("{} > ".format(soma), end="")
    pt = st
    st = soma
print("Acabou")