# Lista com as profissões dos gafanhotos e seus respectivos quantitativos
select profissao, count(*) as quantidade from gafanhotos
group by profissao;