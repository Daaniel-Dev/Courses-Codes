dinheiro = round(float(input('Digite o seu valor em dinheiro (R$): ')), 2)
dolár = 5.67
conversão = round(dinheiro/ dolár, 2)
print(f'Com R$ {dinheiro:.2f} você consegue comprar US$ {conversão:.2f}.')