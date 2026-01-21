"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""


"""
Problema 1
Implementar un sitio WEB en PHP que retorne un archivo con formato JSON con los datos de diferentes artículos.

Para resolver el problema debemos tener un conocimiento del lenguaje PHP y del gestor de base de datos MySQL.

Cree una base de datos llamada 'pythonya' y una tabla 'articulos' con los siguientes datos:

CREATE TABLE `articulos` (
  `codigo` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(50) DEFAULT NULL,
  `precio` float DEFAULT NULL,
  PRIMARY KEY (`codigo`)
);

insert into `articulos` values (1,'papas',15);
insert into `articulos` values (2,'manzanas',24);
insert into `articulos` values (3,'peras',45.3);
insert into `articulos` values (4,'naranjas',22);
insert into `articulos` values (5,'pomelos',29);
insert into `articulos` values (6,'frutillas',130);
insert into `articulos` values (7,'anana',75);
Seguidamente proceda a codificar el siguiente archivo PHP que se conecta a la base de datos 'pythonya', recupera todas las filas de la tabla 'articulos' y finalmente retorna todos los datos en formato JSON:
Programa: retornararticulos.php
<?php
header('Content-Type: application/json');

$server="localhost";
$usuario="root";
$clave="";
$base="pythonya";
$conexion=mysqli_connect($server,$usuario,$clave,$base) or die("problemas") ;
mysqli_set_charset($conexion,'utf8'); 

$datos = mysqli_query($conexion, "SELECT codigo, descripcion, precio from articulos");
$resultado = mysqli_fetch_all($datos, MYSQLI_ASSOC);
echo json_encode($resultado);        
?>


"""

from urllib import request
import json

pagina=request.urlopen("http://localhost/pythonya/retornararticulos.php")
datos=pagina.read().decode("utf-8")
print(datos) # imprimimos un string
print("_"*100)
lista=json.loads(datos) # convertimos el string a una lista
print(lista) # imprimimos una lista
print("_"*100)
for elemento in lista:
    print(f"{elemento['codigo']}  {elemento['descripcion']:50}  {elemento['precio']:>12}")
