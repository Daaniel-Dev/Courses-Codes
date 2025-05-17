cidade = str(input('Digite o nome de uma cidade: ')).strip().title()
if cidade.upper().split()[0] == 'SANTO':
    validação = True
else:
    validação = False
print(f'A cidade {cidade} {'não ' if not validação else ''}começa com o nome "Santo".')

