# Login do usuário e do vendedor em andamento
# Cadastro do vendedor em andamento
from functions import *
titulo('Template', '-', 96)
clientes = list()
vendedores = list()
while True:
    opção = menu_usuario()
    if opção == 0:
        opção = menu_inicial()
        if opção == 0:
            print('WIP')
        elif opção == 1:
            clientes.append(cadastramento_cliente())
        elif opção == 3:
            continue
    elif opção == 1:
        print('WIP')
    elif opção == 2:
        print('Até mais!')
        break






