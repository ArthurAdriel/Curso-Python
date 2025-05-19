cont_idade = cont_homem = cont_mulher = 0
while True:
    print("-" * 25)
    print("   CADASTRE UMA PESSOA   ")
    print("-" * 25)
    idade = int(input("Idade: "))
    sexo = " "
    while sexo not in "FM":
        sexo = str(input("Sexo: [F/M] ")).strip().upper()
    if idade >= 18:
        cont_idade = cont_idade + 1
    if sexo == "M":
        cont_homem = cont_homem + 1
    if sexo == "F" and idade < 20:
        cont_mulher = cont_mulher + 1
    sair = " "
    while sair not in "SN":
        sair = str(input("Quer continuar? [S/N] ")).strip().upper()
    if sair == "N":
        break
print("====== FIM DO PROGRAMA ======")
print(f"Total de pessoas com mais de 18 anos: {cont_idade}")
print(f"Ao todo temos {cont_homem} homens cadastrados. ")
print(f"E temos {cont_mulher} mulheres com menos de 20 anos.")
