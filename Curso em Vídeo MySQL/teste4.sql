# Criar tabela se já não existir outra com mesmo nome
create table if not exists cursos (
nome varchar(30) not null unique,
descricao text,
carga int unsigned,
totaulas int unsigned,
ano year default '2025',
primary key (id_curso))
default charset = utf8mb4;


# Adicionar campo que será a chave primária
alter table cursos
add column id_curso int not null first;


# Alterar sua propriedade para chave primária
alter table cursos
add primary key (id_curso);


# Deixar como auto incrementável
alter table cursos
modify column id_curso int not null auto_increment;