numeração_decimal = 'Unidade', 'Dezena', 'Centena', 'Milhar'
num = int()
while True:
    try:
        num = int(input('Digite um número inteiro entre 0 e 9999: '))
    except ValueError:
        print('\033[31;1mValor inválido. Tente novamente.\033[m')
        continue
    if num < 0 or num > 9999:
        print('\033[31;1mValor inválido. O número deve estar no intervalo especificado.\033[m')
        continue
    break
num = str(num)
for indice, digito in zip(numeração_decimal, num):
    print(f'{indice}: {digito}')


