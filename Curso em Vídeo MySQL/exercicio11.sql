# Lista de gafanhotos homens e mulheres que nasceram após 1 de Janeiro de 2005 
select sexo, count(*) as total_pessoas from gafanhotos where nascimento > '2005-01-01'
group by sexo;