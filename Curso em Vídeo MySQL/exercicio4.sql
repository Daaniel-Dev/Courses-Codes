# Lista de todas as mulheres que nasceram no Brasil e que tem seu nome iniciando com a letra J
select * from gafanhotos where sexo = 'F' 
and nome like 'J%'
and nacionalidade = 'Brasil'