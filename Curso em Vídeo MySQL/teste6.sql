insert into cursos values
('1', 'HTML4', 'Curso de HTML5', '40', '37', '2014'),
('2', 'Algoritmos', 'Logica de Programação', '20', '15', '2014'),
('3', 'Photoshop', 'Dicas de Photoshop CC', '10', '8', '2014'),
('4', 'PGP', 'Curso de PHP para iniciantes', '40', '20', '2010'),
('5', 'Jarva', 'Introdução à Linguagem Java', '10', '29', '2000'),
('6', 'MySQL', 'Banco de Dados MySQL', '30', '15', '2016'),
('7', 'Word', 'Curso completo de Word', '40', '30', '2016'),
('8', 'Sapateado', 'Danças Rítmicas', '40', '30', '2018'),
('9', 'Cozinha Árabe', 'Aprenda a fazer Kibe', '40', '30', '2018'),
('10', 'Youtuber', 'Gerar polêmica e ganhar inscritos', '5', '2', '2018');

select * from cursos;

# Alterar registro de tabela
update cursos
set nome = 'HTML5'
where id_curso = '1';

update cursos
set nome = 'PHP',
ano = '2015'
where id_curso = '4';

update cursos
set nome = 'Java',
carga = '40',
ano = '2015'
where id_curso = '5'
limit 1;


# Deletar registro de tabela
delete from cursos
where id_curso = '8';

delete from cursos 
where id_curso = '9';

delete from cursos
where id_curso = '10';


# Deletar todas os registros de uma tabela
truncate table cursos;












