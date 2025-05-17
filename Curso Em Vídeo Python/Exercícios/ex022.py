nome = str(input('Digite seu nome completo: ')).strip().title().split()
nome = ' '.join(nome)
print(f'''Nome com todas as letras maiúsculas: {nome.upper()} 
Nome com todas as letras minúsculas: {nome.lower()}
Quantidade de letras no nome ao todo: {len(nome.replace(' ', ''))}
Quantidade de letras no primeiro nome: {len(nome.split()[0])}''')
