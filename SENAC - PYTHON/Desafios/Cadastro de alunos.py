from Funções.cadastro import *
from Funções.interface import *
aluno = dict()
sala = list()
soma = contador = 0
titulo('CADASTRO DE TURMA', '-', 35, True)
while True:
    aluno['nome'] = checar_nome()
    aluno['nota'] = checar_nota()
    sala.append(aluno.copy())
    aluno.clear()
    while True:
        confirmação = confirm()
        if confirmação == 'S':
            print('\033[1mReiniciando cadastro...\033[m')
            break
        elif confirmação == 'N':
            tamanho_sala = len(sala)
            titulo('LISTA DE ALUNOS E NOTAS', '-', 35)
            print(f'{'NOME':<30} {'NOTA':<10}')
            print()
            for estudante in sala:
                print(f'{estudante['nome']:<30} {nota_formatada(estudante['nota']):<10}')
                soma = soma + estudante['nota']
            média = soma / tamanho_sala
            titulo(f'MÉDIA DA TURMA: {nota_formatada(média)}', '-', 35)
            titulo('ALUNOS ACIMA DA MÉDIA', '-', 35)
            for estudante in sala:
                if estudante['nota'] > média:
                    contador += 1
                    print(f'{estudante['nome']} ({nota_formatada(estudante['nota'])})')
            if contador == 0:
                print('Nenhum aluno está acima da média.')
            exit(0)

