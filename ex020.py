from random import shuffle
alunos = []
for ordem in range(1, 5):
    alunos.append(input(f'Digite o nome do aluno {ordem}: ').strip().title())
shuffle(alunos)
print('Ordem sorteada: ')
for indice, aluno in enumerate(alunos):
    print(f'Aluno {indice + 1}: {aluno}')