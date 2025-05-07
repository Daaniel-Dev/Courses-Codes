valor = input('Digite algo: ')
print(f'O valor {valor} é do tipo {type(valor)} e tem as seguintes características:')
print(f'Alfanumérico') if valor.isalnum() else ''
print('Alfabético') if valor.isalpha() else ''
print('ASCII') if valor.isascii() else ''
print('Identificador') if valor.isidentifier() else ''
print('Numérico') if valor.isnumeric() else ''
print('Printável') if valor.isprintable() else ''
print('Maiúsculo') if valor.isupper else ''
print('Espaço') if valor.isspace() else ''
print('Decimal') if valor.isdecimal() else ''
print('Minúsculo') if valor.islower() else ''
print('Digito') if valor.isdigit() else ''
print('Título') if valor.istitle() else ''
