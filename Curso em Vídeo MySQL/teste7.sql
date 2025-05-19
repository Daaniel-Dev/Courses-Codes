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


# Usando o operador LIKE para nomes que começam com a letra 'P'
select * from cursos
where nome like 'P%';


# Usando o operador LIKE para nomes que terminam com a letra 'A'
select * from cursos
where nome like '%A';


# Usando o operador LIKE para nomes que contenham ao menos uma letra 'A'
select * from cursos
where nome like '%A%';


# Usando o operador LIKE para nomes que contenham nenhuma letra 'A'
select * from cursos
where nome not like '%A%';


# Usando o operador LIKE para nomes que começam com 'PH' e e terminam com a letra 'P'
select * from cursos
where nome like 'PH%P';
