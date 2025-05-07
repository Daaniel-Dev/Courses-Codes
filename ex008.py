numero = float(input('Digite um valor (Metros): '))
medidas = 'km', 'hm', 'dam', 'm', 'dm', 'cm', 'mm'
contador = 1000
for indice in medidas:
    transformação = numero * contador
    print(f'{indice}: {round(transformação, 3)}')
    contador /= 10




