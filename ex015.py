km = int(input('Quilômetros rodados com o carro: '))
dias = int(input('Quantidade de dias alugados: '))
preço_total = (km * 0.15) + (dias * 60)
print(f'Preço total a pagar: R$ {preço_total:.2f}')