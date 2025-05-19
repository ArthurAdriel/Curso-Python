pt = int(input("Qual será o primeiro termo? "))
rz = int(input("Qual será a razão? "))
cont = 0 
resposta = pt
mais = 10
total = 0
while mais != 0:
    total = mais + total
    while cont < total:
        print("{} > ".format(resposta), end="")
        resposta = resposta + rz
        cont = cont + 1 
    print("Pausa")
    mais = int(input("Mais quantos termos você quer adicionar? "))
print("Acabou")
