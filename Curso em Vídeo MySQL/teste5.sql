create table if not exists teste (
id int not null auto_increment,
nome varchar(30) not null,
nascimento date,
primary key (id)
);

insert into teste values
('Enzo', '2010-06-23'),
('Joana', '1982-05-18'),
('Carlos', '2000-09-30');


# Remover tabela
drop table if exists teste;