def checar_nome():
    while True:
        x = str(input('Nome: ')).strip().title()
        if x.isnumeric() or x.isspace() or len(x) == 0:
            print('\033[31;1mValor inválido. Digite novamente.\033[m')
        else:
            print('\033[32;1mValor cadastrado com sucesso!\033[m')
            return x


def checar_nota():
    while True:
        while True:
            try:
                x = float(input('Nota: '))
            except ValueError:
                print('\033[31;1mValor inválido. Digite um número.\033[m')
            else:
                if x > 10 or x < 0:
                    print('\033[31;1mValor inválido. Digite um número entre 0 e 10.\033[m')
                    break
                else:
                    print('\033[32;1mValor cadastrado com sucesso!\033[m')
                    return round(x, 1)


def pergunta_multiplas_escolhas(*escolhas, nome):
    lista = []
    while True:
        while True:
            for indice, x in enumerate(escolhas):
                lista.append(indice)
                print(f'[{indice}] {x.upper()}', end=' | ' if x != escolhas[-1] else '\n')
            try:
                pergunta = int(input(f'Você é de qual {nome}?\n'))
            except ValueError:
                print('\033[31;1mValor inválido. Tente novamente.\033[m')
            else:
                if pergunta not in lista:
                    print(f'\033[31;1mValor inválido. Digite um número entre 0 e {len(escolhas) - 1}.\033[m')
                    break
                else:
                    print('\033[32;1mValor cadastrado com sucesso!\033[m')
                    return pergunta


def confirm():
    while True:
        x = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if x not in ('S', 'N'):
            print('\033[31;1mValor inválido. Digite S ou N.\033[m')
        else:
            return x


def nota_formatada(nota):
    return str(nota).replace('.', ',')