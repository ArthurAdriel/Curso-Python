import moeda

resp = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(resp)} é {moeda.metade(resp, False)}')
print(f'O dobro de {moeda.moeda(resp)} é {moeda.dobro(resp, True)}')
print(f'Aumentando 10% fica em {moeda.aumentar(resp, 10, True)}')
print(f'Diminuindo em 13% fica em {moeda.diminuir(resp, 13, False)}')
