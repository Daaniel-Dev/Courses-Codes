# Em andamento

def titulo(msg, linha, espaco):
    msg = f'{msg:^{espaco}}'
    print(f'{linha}' * len(msg))
    print(msg)
    print(f'{linha}' * len(msg))


def menu(*escolhas):
    lista = []
    while True:
        for indice, nomes in enumerate(escolhas):
            lista.append(indice)
            print(f'[{indice + 1}] {nomes.upper()}', end='\n')
        try:
            pergunta = int(input(f'Deseja realizar qual ação?\n')) - 1
        except ValueError:
            print('\033[31;1mValor inválido. Tente novamente.\033[m')
            continue
        if pergunta not in lista:
            print(f'\033[31;1mValor inválido. Digite um número entre 1 e {len(escolhas)}.\033[m')
            continue
        return pergunta

def cadastro():
    while True:
        nome = str(input('Nome: ')).strip().title()
        if nome.isnumeric() or nome.isspace() or not nome:
            print('\033[31;1mValor inválido. Digite novamente.\033[m')
            continue
        print('\033[32;1mValor cadastrado com sucesso!\033[m')
    while True:
        cpf = str(input('CPF: ')).strip().








