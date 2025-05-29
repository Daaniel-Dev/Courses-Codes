# Lista mostrando a altura máxima entre homens brasileiros
select max(altura) from gafanhotos where nacionalidade = 'Brasil' and sexo = 'M'