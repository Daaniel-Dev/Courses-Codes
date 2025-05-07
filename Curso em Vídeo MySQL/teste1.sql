# Criar banco de dados com suporte para acentuação
create database cadastro
default character set utf8mb4
default collate utf8mb4_general_ci;


# Criar tabela 
create table pessoas (
id_pessoa int not null auto_increment,
nome varchar(30),
nascimento date,
sexo enum('M', 'F'),
altura decimal(3, 2),
peso decimal(5, 2),
nacionalidade varchar(20) default 'Brasil',
primary key (id_pessoa))
default charset = utf8mb4