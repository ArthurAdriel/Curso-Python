sexo = str(input('Qual o seu sexo? [F/M] ')).strip().upper() [0]
while sexo not in "FM":
    sexo = str(input("Dados inválidos! Qual o seu sexo? ")).strip().upper() [0]
print("Seu sexo é {}.".format(sexo))
