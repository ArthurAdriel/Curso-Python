total = 0 
mais_velho = 0 
cont_nova = 0 
nome_velho = ""
for c in range(1, 5):
    print('----- {}° PESSOA -----'.format(c))
    nome = str(input('NOME: '))
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [H/M]: '))
    total += idade
    if sexo == 'M' and idade < 20:
        cont_nova += 1
    if sexo == 'H' and idade > mais_velho:
        mais_velho = idade
        nome_velho = nome
media = total / 4
print('O homem mais velho é o {}, com {} anos!'.format(nome_velho, mais_velho))
print('A média de idade desse grupo é de {} anos.'.format(media))
print('Nesse grupo tem {} mulheres com menos de 20 anos.'.format(cont_nova))
