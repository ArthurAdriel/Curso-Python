n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
if media >= 7:
    print('Você está aprovado! Parabéns!')
elif media >= 5 or media < 7:
    print('Você está de recuperação.')
else:
    print('Infelizmente você está reprovado.')
