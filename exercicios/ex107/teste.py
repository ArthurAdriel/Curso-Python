import moeda

resp = float(input('Digite o preço: R$'))
print(f'A metade de {resp} é {moeda.metade(resp)}')
print(f'O dobro de {resp} é {moeda.dobro(resp)}')
print(f'Aumentando 10% fica em {moeda.aumentar(resp, 10)}')
print(f'Diminuindo em 13% fica em {moeda.diminuir(resp, 13)}')
