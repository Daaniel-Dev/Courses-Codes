# Ecora - Sua Plataforma de Produtos Sustentáveis

## Descrição

**Ecora** é uma aplicação simples e eficiente desenvolvida em **Python**, com o objetivo de ser um **marketplace de produtos sustentáveis**. A proposta é criar um ambiente onde grandes e pequenos vendedores possam divulgar seus produtos, promovendo práticas conscientes e ecológicas.

Os usuários podem se cadastrar como:

- **Clientes**: exploram os produtos e realizam compras.
- **Vendedores**: cadastram produtos, com opção de adicionar vídeos sobre o uso ou propósito do item.

Além disso, a plataforma oferece espaço para:

- Depoimentos de usuários
- Vídeos educacionais sobre sustentabilidade

---

## Funcionalidades

- Cadastro de clientes e vendedores
- Cadastro de produtos com nome, preço, descrição e vídeo opcional
- Exibição e compra de produtos
- Compartilhamento de depoimentos dos usuários
- Gerenciamento de vídeos educacionais
- Seção "Sobre Nós", com informações do aplicativo

---

## Objetivo

Nosso objetivo é ser um marketplace acessível, promovendo visibilidade para todos os tipos de vendedores, incentivando a economia circular e a educação ambiental. Buscamos conscientizar os usuários sobre o destino correto de produtos sem utilidade e como reutilizá-los de forma criativa e consciente.

---

## Estrutura do Projeto

- `main.py`: gerencia o fluxo principal do programa (menus, navegação e controle)
- `functions.py`: contém funções auxiliares (cadastro, exibição e manipulação de dados)
- `classes.py`: define as classes principais:
  - `User`: classe base para usuários
  - `Cliente`: herda de `User`
  - `Vendedor`: herda de `User`, com permissão para cadastrar produtos
  - `Produto`: representa os itens à venda

---

## Sobre Nós
O Ecora foi desenvolvido com o propósito de conectar pessoas, ideias e atitudes sustentáveis, usando a tecnologia como ponte para um futuro mais consciente.

