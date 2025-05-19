import random
print('Vamos jogar jokenpô?')
jok = ['pedra', 'papel', 'tesoura']
escm = random.choice(jok)
esch = str(input('Você vai escolher pedra, papel ou tesoura? ')).lower()
if escm == esch:
    print('Nós dois escolhemos {}. Portanto deu empate.'.format(escm))
elif escm == 'pedra' and esch == 'tesoura':
    print('Eu escolhi Pedra e você escolheu tesoura. Então eu ganhei.')
elif esch == 'pedra' and escm == 'tesoura':
    print('Você escolheu pedra e eu escolhi tesoura. Então você ganhou!')
elif escm == 'papel' and esch == 'pedra':
    print('Eu escolhi Papel e você escolheu Pedra. Então eu ganhei de você.')
elif esch == 'papel' and escm == 'pedra':
    print('Você escolheu Papel e eu escolhi Pedra. Então você ganhou!')
elif escm == 'tesoura' and esch == 'papel':
    print('Eu escolhi Tesoura e você escolheu Papel. Então eu ganhei de você.')
elif esch == 'tesoura' and escm == 'papel':
    print('Você escolheu Tesoura e eu escolhi Papel. Então você ganhou!')
else:
    print('Você digitou errado!')
