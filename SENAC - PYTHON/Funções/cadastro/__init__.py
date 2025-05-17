def checar_nome():
    while True:
        nome = str(input('Nome: ')).strip().title()
        if nome.isnumeric() or nome.isspace() or len(nome) == 0:
            print('\033[31;1mValor inválido. Digite novamente.\033[m')
            continue
        print('\033[32;1mValor cadastrado com sucesso!\033[m')
        return nome


def checar_nota():
    while True:
        try:
            nota = float(input('Nota: '))
        except ValueError:
            print('\033[31;1mValor inválido. Digite um número.\033[m')
            continue
        if nota > 10 or nota < 0:
            print('\033[31;1mValor inválido. Digite um número entre 0 e 10.\033[m')
            continue
        print('\033[32;1mValor cadastrado com sucesso!\033[m')
        return round(nota, 1)


def pergunta_multiplas_escolhas(*escolhas, nome):
    lista = []
    while True:
        for indice, x in enumerate(escolhas):
            lista.append(indice)
            print(f'[{indice}] {x.upper()}', end=' | ' if x != escolhas[-1] else '\n')
        try:
            pergunta = int(input(f'Você é de qual {nome}?\n'))
        except ValueError:
            print('\033[31;1mValor inválido. Tente novamente.\033[m')
            continue
        if pergunta not in lista:
            print(f'\033[31;1mValor inválido. Digite um número entre 0 e {len(escolhas) - 1}.\033[m')
            continue
        print('\033[32;1mValor cadastrado com sucesso!\033[m')
        return pergunta


def confirm():
    while True:
        confirmação = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if confirmação not in ('S', 'N'):
            print('\033[31;1mValor inválido. Digite S ou N.\033[m')
            continue
        return confirmação


def nota_formatada(nota):
    return str(nota).replace('.', ',')
