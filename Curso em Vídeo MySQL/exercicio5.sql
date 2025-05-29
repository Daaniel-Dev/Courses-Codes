# Lista de todos os homens que possuem 'Silva' no nome, não são do Brasil e tem peso menor que 100kg
select nome, nacionalidade from gafanhotos where sexo = 'M' 
and nome 
like '%Silva%' 
and nacionalidade != 'Brasil' 
and peso < 100;
