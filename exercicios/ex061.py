pt = int(input("Qual será o primeiro termo? "))
rz = int(input("Qual será a razão? "))
cont = 0 
resposta = pt
while cont < 10:
    print("{} > ".format(resposta), end="")
    resposta = resposta + rz
    cont = cont + 1 
print("Acabou")