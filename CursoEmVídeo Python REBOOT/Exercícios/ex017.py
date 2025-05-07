from math import hypot
cat_oposto = float(input('Digite o cateto oposto de um triângulo: '))
cat_adjacente = float(input('Digite o cateto adjacente de um triângulo: '))
hipotenusa = hypot(cat_oposto, cat_adjacente)
print(f'A hipotenusa do triângulo descrito é: {round(hipotenusa, 2)}')