from random import choices
alunos = []
for ordem in range(1, 5):
    alunos.append(input(f'Digite o nome do aluno {ordem}: ').strip().title())
escolha = choices(alunos)
print('Alunos cadastrados:')
for aluno in alunos:
    print(aluno)
print(f'Aluno escolhido: {escolha[0]}')