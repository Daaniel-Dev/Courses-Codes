from classes import *

def titulo(msg, linha, espaco):
    msg = f'{msg:^{espaco}}'
    print(f'{linha}' * len(msg))
    print(msg)
    print(f'{linha}' * len(msg))


def menu(*escolhas, msg):
    lista = []
    while True:
        for indice, nomes in enumerate(escolhas):
            lista.append(indice)
            print(f'[{indice + 1}] {nomes.upper()}', end='\n')
        try:
            pergunta = int(input(f'{msg}\n')) - 1
        except ValueError:
            print('\033[31;1mValor inválido. Tente novamente.\033[m')
            continue
        if pergunta not in lista:
            print(f'\033[31;1mValor inválido. Digite um número entre 1 e {len(escolhas)}.\033[m')
            continue
        return pergunta


def menu_inicial():
    print('-' * 96)
    return menu('LOGIN', 'CADASTRO', 'SAIR', 'VOLTAR', msg='Deseja realizar qual ação?')


def menu_usuario():
    print('-' * 96)
    return menu('CLIENTE', 'VENDEDOR', 'SAIR', msg='Você é cliente ou vendedor?')


def cadastro_nome():
    while True:
        nome = str(input('Como devemos te chamar?\n')).strip().title()
        if nome.isnumeric() or nome.isspace() or not nome:
            print('\033[31;1mNome inválido. Tente novamente.\033[m')
            continue
        print('\033[32;1mNome cadastrado com sucesso!\033[m')
        return nome


def cadastro_cpf():
    def calcular_digito(cpf_inf, digito1=True):
        lista = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        somatorio = 0
        for conjunto in zip(cpf_inf, lista[1:] if digito1 else lista):
            somatorio = somatorio + int(conjunto[0]) * conjunto[1]
        resto_digito = somatorio % 11
        resto_digito = 0 if resto_digito == 10 else resto_digito
        return resto_digito
    while True:
        cpf = (str(input('Cadastre seu CPF:\n')).strip().replace('.', '')
               .replace('-', ''))
        if len(cpf) != 11 or not cpf.isnumeric():
            print('\033[31;1mCPF inválido. É necessário 11 dígitos numéricos.\033[m')
        elif len(cpf) == 11 and cpf.isnumeric():
            primeiro_digito = calcular_digito(cpf, True)
            segundo_digito = calcular_digito(cpf, False)
            dv_modulo_11_informado = cpf[9:]
            dv_modulo_11_calculado = str(primeiro_digito) + str(segundo_digito)
            if dv_modulo_11_informado == dv_modulo_11_calculado :
                print('\033[32;1mCPF cadastrado com sucesso!\033[m')
                return cpf
            else:
                print('\033[31;1mCPF inválido. Tente novamente.\033[m')


def cadastro_senha():
    print('\033[1mATENÇÃO!\033[m '
          'Só é permitido o uso de letras (a-z), números (0-9) e o arroba (@) na criação da senha.'
          '\nAlém disso, o arroba não pode estar no começo da senha.')
    while True:
        senha = str(input('Cadastre sua senha:\n')).strip()
        if not senha.replace('@', '').isalnum() or senha.find('@') == 0:
            print('\033[31;1mSenha inválida. Tente novamente.\033[m')
        elif senha.replace('@', '').isalnum() and senha.find('@') != 0:
            verificacao1 = menu('CONTINUAR', 'INFORMAR OUTRA',
                                               msg='Deseja continuar com essa senha ou informar outra?')
            if verificacao1 == 0:
                while True:
                    verificacao2 = str(input('Digite a senha que você acabou de cadastrar\n')).strip()
                    if verificacao2 != senha:
                        print('As senhas não correspondem.')
                    else:
                        print('\033[32;1mSenha cadastrada com sucesso!\033[m')
                        return senha
            elif verificacao1 == 1:
                continue


def cadastramento_cliente():
    clientes = list()
    dados_cadastro = dict()
    keys = 'cpf', 'senha', 'nome'
    funções_cadastro_cliente = cadastro_cpf(), cadastro_senha(), cadastro_nome()
    for values in zip(keys, funções_cadastro_cliente):
        dados_cadastro[values[0]] = values[1]
    print('\033[1mCadastro finalizado!\033[m')
    cliente = User(dados_cadastro['cpf'], dados_cadastro['senha'], dados_cadastro['nome'])
    return cliente

def login_cpf_cliente():
    while True:
        cpf = (str(input('CPF:\n')).strip().replace('.', '')
               .replace('-', ''))
        if len(cpf) != 11 or not cpf.isnumeric():
            print('\033[31;1mCPF inválido. É necessário 11 dígitos numéricos.\033[m')
        elif len(cpf) == 11 and cpf.isnumeric():
            return cpf


def login_senha_cliente():
    while True:
        senha = str(input('Senha:\n')).strip()
        if not senha.replace('@', '').isalnum() or senha.find('@') == 0:
            print('\033[31;1mSenha inválida. Tente novamente.\033[m')
        elif senha.replace('@', '').isalnum() and senha.find('@') != 0:
            return senha

