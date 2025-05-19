alt = float(input('Qual a sua altura? '))
pes = float(input('Qual o seu peso? '))
imc = pes / (alt * alt)
if imc < 18.5:
    print('Você está abaixo do peso! ')
elif imc >= 18.5 and imc < 25:
    print('Você está no seu peso ideal! Parabéns! ')
elif imc >= 25 and imc < 30:
    print('Você está sobrepeso. ')
elif imc > 30 and imc < 40:
    print('Você está sofrendo com obesidade. Procure um médico. ')
else:
    print('Você está com obesidade mórbida! Procure um médico urgente! ')
