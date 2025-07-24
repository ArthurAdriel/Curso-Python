from time import sleep

def maior(* numeros):
    print('-=' * 30)
    print('Analisando os valores passados... ')
    for c in numeros:
        print(f'{c}', end=' ', flush=True)
        sleep(0.3)
    print(f'Foram informados {len(numeros)} valores ao todo.')
    print(f'E o maior valor foi {max(numeros)}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)
