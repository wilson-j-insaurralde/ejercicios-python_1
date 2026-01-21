"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""


"""
Ingresar por teclado el código de un artículo, seguidamente recuperar los datos de dicho artículo del servidor local. Pasar el código del artículo como parámetro 'GET' en la llamada.

La aplicación en PHP que recupera los datos de un determinado artículo que llega como parámetro es:

Programa: retornararunarticulo.php
"""

"""
<?php
header('Content-Type: application/json');

$server="localhost";
$usuario="root";
$clave="";
$base="pythonya";
$conexion=mysqli_connect($server,$usuario,$clave,$base) or die("problemas") ;
mysqli_set_charset($conexion,'utf8'); 

$datos = mysqli_query($conexion, "SELECT codigo, descripcion, precio from articulos where codigo=$_GET[codigo]");
$resultado = mysqli_fetch_all($datos, MYSQLI_ASSOC);
echo json_encode($resultado);        
?>
"""



from urllib import request
import json

codigo=input("Ingrese el código de artículo a consultar:")
pagina=request.urlopen(f"http://localhost/pythonya/retornarunarticulo.php?codigo={codigo}")
datos=pagina.read().decode("utf-8")
lista=json.loads(datos)
if len(lista)>0:
    print(f"Descripción:{lista[0]['descripcion']}")
    print(f"Precio:{lista[0]['precio']}")
else:
    print("No existe un artículo con el código ingresado")