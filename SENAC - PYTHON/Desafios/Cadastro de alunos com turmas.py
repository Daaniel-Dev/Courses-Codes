from Funções.cadastro import *
from Funções.interface import *
aluno = dict()
maior_nota = {}
salas = {'mobile': [], 'algoritmo': [], 'web': [], 'jogos': [], 'gestão de projetos': []}
titulo('CADASTRO DE TURMA', '-', 40, True)
while True:
    aluno['nome'] = checar_nome()
    aluno['nota'] = checar_nota()
    pergunta = pergunta_multiplas_escolhas(*salas, nome='sala')
    for value in range(len(salas)):
        if pergunta == value:
            salas[f'{list(salas)[value]}'].append(aluno.copy())
    while True:
        confirmação = confirm()
        if confirmação == 'S':
            print('\033[1mReiniciando cadastro...\033[m')
            break
        elif confirmação == 'N':
            for nome_sala, estudantes in salas.items():
                print()
                soma = contador = 0
                tamanho_sala = len(salas[nome_sala])
                titulo(f'ALUNOS DA TURMA {nome_sala.upper()}', '-', 40, True)
                if tamanho_sala > 0:
                    print(f'{'NOME':<35} {'NOTA':<10}')
                    print()
                    for ordem, estudante in enumerate(estudantes):
                        if ordem == 0 and not maior_nota:
                            maior_nota = estudante
                        elif estudante['nota'] > maior_nota['nota']:
                            maior_nota = estudante
                        print(f'{estudante['nome']:<35} {nota_formatada(estudante['nota']):<10}')
                        soma = soma + estudante['nota']
                    média = soma / tamanho_sala
                    titulo(f'MÉDIA DA TURMA {nome_sala.upper()}: {nota_formatada(média)}', '-', 40)
                    titulo('ALUNOS ACIMA DA MÉDIA', '-', 40)
                    for estudante in estudantes:
                        if estudante['nota'] > média:
                            contador = contador + 1
                            print(f'- {estudante['nome']} ({nota_formatada(estudante['nota'])})')
                    if contador == 0:
                        print('- Não há alunos acima da média\nnessa turma.')
                else:
                    print('- Não há alunos cadastrados\nnessa turma.')
            print()
            print('-' * 40)
            print(f'Melhor aluno geral: {maior_nota['nome']} ({nota_formatada(maior_nota['nota'])})')
            print('-' * 40)
            print('Volte sempre!')
            exit(0)
