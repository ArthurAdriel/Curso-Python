num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite outro número: '))
num4 = int(input('Digite outro número: '))
numeros = num1, num2, num3, num4
print(f'Você digitou os números {numeros}')
print(f'O número 9 apareceu {numeros.count(9)} vezes.')
if numeros.count(3) == 0:
    print('Você não digitou nenhuma vez o número 3.')
else:
    print(f'O número 3 está na {numeros.index(3) + 1}° posição. ')
print('Os números pares digitados foram ', end='')
for num in numeros:
    if num % 2 == 0:
        print(num, end=' ')
