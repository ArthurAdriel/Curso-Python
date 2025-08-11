import moeda

resp = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(resp)} é {moeda.moeda(moeda.metade(resp))}')
print(f'O dobro de {moeda.moeda(resp)} é {moeda.moeda(moeda.dobro(resp))}')
print(f'Aumentando 10% fica em {moeda.moeda(moeda.aumentar(resp, 10))}')
print(f'Diminuindo em 13% fica em {moeda.moeda(moeda.diminuir(resp, 13))}')
