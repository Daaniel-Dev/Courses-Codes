# Selecionando por ordem de nome em forma crescente
select * from cursos 
order by nome;


# Selecionando por ordem de nome em forma decrescente
select * from cursos 
order by nome 
desc;


# Selecionando colunas
select nome, carga, ano from cursos 
order by nome;


# Selecionando colunas usando mais de uma ordem
select ano, nome, carga from cursos 
order by ano, nome;


# Selecionando linhas
select * from cursos
where ano = '2016'
order by nome;


# Selecionando linhas e colunas
select nome, descricao, carga from cursos
where ano = '2016'
order by nome;

select nome, descricao from cursos
where ano <= '2015'
order by nome;


# Selecionando intervalos
select * from cursos
where totaulas between '20' and '30';

select nome, ano from cursos
where ano between '2014' and '2016'
order by ano desc, nome;


# Selecionando valores
select idcurso, nome from cursos
where ano in ('2014', '2016', '2018')
order by nome;


# Combinando Testes
select * from cursos
where carga > 35 and totaulas < 30
order by nome;


# Usando o operador LIKE com a wildcard % para nomes que começam com a letra 'P'
select * from cursos
where nome like 'P%';


# Usando o operador LIKE com a wildcard % para nomes que terminam com a letra 'A'
select * from cursos
where nome like '%A';


# Usando o operador LIKE com a wildcard % para nomes que contenham ao menos uma letra 'A'
select * from cursos
where nome like '%A%';


# Usando o operador LIKE com a wildcard % para nomes que contenham nenhuma letra 'A'
select * from cursos
where nome not like '%A%';


# Usando o operador LIKE com a wildcard % para nomes que começam com 'PH' e terminam com a letra 'P'
select * from cursos
where nome like 'PH%P';


# Usando o operador LIKE com a wildcard _ e % para nomes que começam com 'PH', terminam com a letra 'P' e contenham algum caractere no final
select * from cursos
where nome like 'PH%P_';


# Distinguindo registros repetidos
select distinct nacionalidade from gafanhotos;


# Agregação com função count()
select count(*) from cursos where carga > 30;


# Agregação com função max() e min()
select nome, max(totaulas) from cursos where ano = '2016';
select nome, min(totaulas) from cursos where ano = '2016';


# Agregação com função sum()
select sum(totaulas) from cursos;


# Agregação com função avg()
select avg(totaulas) from cursos;


# Agrupando registros com group by
select carga from cursos
group by carga;


# Agrupando e agregando
select carga, count(nome) from cursos
group by carga;
select carga, count(*) from cursos where totaulas = 30
group by carga;
select carga, count(*) from cursos
group by carga having count(*) > 3;
select ano, count(*) from cursos where totaulas > 20
group by ano having ano > 2012
order by count(*) desc;
select carga, count(*) from cursos where ano > 2015
group by carga having carga > (select avg(carga) from cursos);
