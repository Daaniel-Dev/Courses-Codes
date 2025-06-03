from functions import *

titulo('Ecora - Sua plataforma de produtos sustentáveis!')
produtos_gerais = []
while True:
    opcao = menu(
        ['Login (em breve)', 'Cadastrar', 'Ver Produtos e Comprar', 'Sobre Nós', 'Depoimentos', 'Vídeo Educacional', 'Sair'],
        'Escolha uma opção:'
    )

    if opcao == 0:
        print('Função de login em desenvolvimento...')

    elif opcao == 1:
        tipo = menu(['Cliente', 'Vendedor'], 'Você quer se cadastrar como:')
        if tipo == 0:
            cliente = cadastro_usuario('CLIENTE')
            print('Cliente cadastrado com sucesso!')
        else:
            vendedor = cadastro_usuario('VENDEDOR')
            print('Vendedor cadastrado com sucesso!')
            while True:
                acao = menu(['Cadastrar Produto', 'Listar Meus Produtos', 'Sair'], 'Escolha uma ação:')
                if acao == 0:
                    produto = cadastrar_produto(vendedor)
                    produtos_gerais.append(produto)
                elif acao == 1:
                    listar_produtos_disponiveis(vendedor.produtos)
                else:
                    break

    elif opcao == 2:
        comprar_produto(produtos_gerais)

    elif opcao == 3:
        sobre()

    elif opcao == 4:
        funcao_depoimentos()

    elif opcao == 5:
        video_educacional()

    elif opcao == 6:
        print('Obrigado por usar nosso app.')
        break
