nome = str(input('Digite seu nome completo: ')).strip().title().split()
nome = ' '.join(nome)
if nome.upper().find('SILVA') == -1:
    validação = False
else:
    validação = True
print(f'{nome} {'não ' if not validação else ''}possui "Silva" no nome.')