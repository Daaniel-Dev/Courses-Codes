from classes import *


def titulo(texto):
    print('=' * 60)
    print(texto.center(60))
    print('=' * 60)


def menu(opcoes, mensagem):
    for i, opcao in enumerate(opcoes):
        print(f'[{i + 1}] {opcao}')
    while True:
        escolha = input(mensagem + '\n')
        if escolha.isdigit() and 1 <= int(escolha) <= len(opcoes):
            return int(escolha) - 1
        else:
            print('Opção inválida. Tente novamente.')


def sobre():
    titulo('SOBRE NÓS')
    print('''Este é um aplicativo simples para compra e venda de produtos sustentáveis. 
Os usuários podem se cadastrar como clientes ou vendedores. 
Vendedores podem cadastrar produtos, enquanto os clientes podem adquiri-los. 
Nosso objetivo é ser um marketplace que permita tanto grandes quanto pequenos vendedores divulgar seus produtos, 
oferecendo a plataforma ideal para o reconhecimento de seus talentos. 
Além disso, o app permite que usuários e vendedores adicionem vídeos sobre seus produtos. 
Há também uma seção educativa para orientar os usuários sobre como reutilizar ou descartar itens sem utilidade.''')


def cadastro_nome():
    while True:
        nome = input('Digite seu nome: ').strip().title()
        if nome:
            return nome
        else:
            print('Nome inválido. Tente novamente.')


def cadastro_cpf():
    def calcular_digito(cpf_inf, digito1=True):
        lista = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        somatorio = 0
        for conjunto in zip(cpf_inf, lista[1:] if digito1 else lista):
            somatorio += int(conjunto[0]) * conjunto[1]
        resto_digito = somatorio % 11
        resto_digito = 0 if resto_digito == 10 else resto_digito
        return resto_digito
    while True:
        cpf = str(input('Cadastre seu CPF: ')).strip().replace('.', '')
        if len(cpf) != 11 or not cpf.isnumeric():
            print('\033[31;1mCPF inválido. É necessário 11 dígitos numéricos.\033[m')
        else:
            primeiro_digito = calcular_digito(cpf, True)
            segundo_digito = calcular_digito(cpf, False)
            dv_informado = cpf[9:]
            dv_calculado = str(primeiro_digito) + str(segundo_digito)
            if dv_informado == dv_calculado:
                while True:
                    cpf_ja_existente = False
                    try:
                        with open('dados.txt', 'r') as dados:
                            linhas = dados.readlines()
                            break
                    except FileNotFoundError:
                        with open('dados.txt', 'w') as dados:
                            continue
                for linha in linhas:
                    try:
                        dados = eval(linha.strip())
                    except SyntaxError:
                        continue
                    if cpf == dados[0]:
                        cpf_ja_existente = True
                        print(f'\033[31;1mCPF já cadastrado como {dados[3]}. Tente colocar outro.\033[m')
                        break
                if not cpf_ja_existente:
                    print('\033[32;1mCPF cadastrado com sucesso!\033[m')
                    return cpf
            else:
                print('\033[31;1mCPF inválido. Tente novamente.\033[m')


def cadastro_senha():
    while True:
        senha = input('Digite uma senha: ').strip()
        confirm = input('Confirme sua senha: ').strip()
        if senha == confirm:
            return senha
        else:
            print('\003[31;1mAs senhas não conferem. Tente novamente.\033[m')


def cadastro_usuario(tipo):
    cpf = cadastro_cpf()
    senha = cadastro_senha()
    nome = cadastro_nome()
    if tipo == 'CLIENTE':
        usuario = User(cpf, senha, nome)
    elif tipo == 'VENDEDOR':
        usuario = Vendedor(cpf, senha, nome)
    with open('dados.txt', 'a') as dados_usuario:
        dados_usuario.write(f'{usuario.chamar_dados()}\n')


def cadastrar_produto(vendedor):
    nome = input('Nome do produto: ').strip().title()
    descricao = input('Descrição do produto: ').strip()
    preco = float(input('Preço do produto (R$): ').replace(',', '.'))
    url_video = input('Link do vídeo (opcional): ').strip()
    produto = Produto(nome, preco, descricao, url_video)
    vendedor.produtos.append(produto)
    print('Produto cadastrado com sucesso!')
    return produto


def listar_produtos_disponiveis(lista_produtos):
    if not lista_produtos:
        print('Nenhum produto disponível.')
    else:
        for i, prod in enumerate(lista_produtos, start=1):
            print(f'\nProduto [{i}]:\n{prod}\n')


def comprar_produto(lista_produtos):
    if not lista_produtos:
        print('Nenhum produto disponível.')
        return
    listar_produtos_disponiveis(lista_produtos)
    try:
        escolha = int(input('Digite o número do produto que deseja comprar (0 para cancelar): '))
        if escolha == 0:
            print('Compra cancelada.')
            return
        if 1 <= escolha <= len(lista_produtos):
            produto = lista_produtos[escolha - 1]
            print(f'Você escolheu: {produto.nome} - R${produto.preco:.2f}')
            confirmar = input('Deseja comprar? (S/N): ').strip().upper()
            if confirmar == 'S':
                cartao = input('Digite o número do cartão (fictício): ')
                print(f'Compra aprovada no cartão {cartao}!')
                print(f'Obrigado por comprar {produto.nome}!')
            else:
                print('Compra cancelada.')
        else:
            print('Produto não encontrado.')
    except ValueError:
        print('Entrada inválida.')


depoimentos = []

def funcao_depoimentos():
    while True:
        escolha = menu(['Adicionar Depoimento', 'Ver Depoimentos', 'Voltar'], 'Escolha uma opção:')
        if escolha == 0:
            nome = input('Seu nome: ').strip().title()
            comentario = input('Seu depoimento: ').strip()
            if comentario:
                depoimentos.append({'nome': nome, 'comentario': comentario})
                print('Depoimento adicionado com sucesso!')
            else:
                print('Depoimento não pode ser vazio.')
        elif escolha == 1:
            if not depoimentos:
                print('Nenhum depoimento ainda.')
            else:
                print('\n--- Depoimentos ---\n')
                for d in depoimentos:
                    print(f'{d["nome"]} disse: "{d["comentario"]}"\n')
        else:
            break


videos_educacionais = []

def video_educacional():
    while True:
        escolha = menu(['Adicionar Link', 'Ver Links', 'Voltar'], 'Escolha uma opção:')
        if escolha == 0:
            link = input('Cole o link do seu vídeo educacional: ').strip()
            if link:
                videos_educacionais.append(link)
                print('Link adicionado com sucesso!')
            else:
                print('Link não pode estar vazio.')
        elif escolha == 1:
            if not videos_educacionais:
                print('Nenhum link cadastrado.')
            else:
                print('\n--- Vídeos Educacionais ---')
                for i, link in enumerate(videos_educacionais, start=1):
                    print(f'{i}. {link}')
                print()
        else:
            break

#def login(cpf, senha):
