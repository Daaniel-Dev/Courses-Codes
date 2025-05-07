# Adicionar campo na tabela
alter table pessoas
add column profissao varchar(10);


# Remover campo da tabela
alter table pessoas
drop column profissao;


# Adicionar campo depois de outro na tabela
alter table pessoas
add column profissao varchar(10) after nome;


# Adicionar campo como primeiro na tabela
alter table pessoas
add column codigo int first;


# Modificar campo da tabela
alter table pessoas
modify column profissao varchar(20);


# Renomear campo da tabela
alter table pessoas
change column profissao prof varchar(20);


# Renomear tabela
alter table pessoas
rename to gafanhotos;





