frase = str(input('Digite uma frase: ')).strip()
contador = frase.count('A')
posição_inicial = frase.find('A')
posição_final = frase.find('A', )

print(f"""Quantidade de letras "A": {contador}
Primeira ocorrência da letra "A": {posição_inicial}
Última ocorrência da letra "A": {posição_final}""")
