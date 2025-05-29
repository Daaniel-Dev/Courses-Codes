# Lista mostrando o menor peso entre mulheres não brasileiras e nascidas entre 1 de Janeiro de 1990 e 31 de Dezembro de 2000
select min(peso) from gafanhotos where nacionalidade != 'Brasil'
and sexo = 'F'
and nascimento between '1990-01-01' and '2000-12-31';