# Lista de pessoas que nasceram entre 1 de Janeiro de 2000 e 31 de Dezembro de 2015
select nome, nascimento from gafanhotos where nascimento between '2000-01-01' and '2015-12-31'
order by nascimento;
