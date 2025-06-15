# Lista agrupada pela altura dos gafanhotos que mostra quais pesam mais de 100kg e que estão acima da média de altura de todos os cadastrados
select altura, count(*) as total_acima_100kg from gafanhotos where peso > 100
group by altura
having altura > (select avg(altura) from gafanhotos);
