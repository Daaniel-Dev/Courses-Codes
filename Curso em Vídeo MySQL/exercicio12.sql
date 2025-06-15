# Lista dos gafanhotos que nasceram fora do Brasil,
# mostrando o país de origem e o total de pessoas nascidas lá apenas dos países com mais de 3 pessoas com a nacionalidade
select nacionalidade, count(*) as total_pessoas from gafanhotos where nacionalidade != 'Brasil'
group by nacionalidade
having count(*) > 3;