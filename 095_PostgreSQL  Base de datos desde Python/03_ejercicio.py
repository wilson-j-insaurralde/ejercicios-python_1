
"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""


"""
Borrado y modificación de filas.
Las otras dos actividades fundamentales que podemos hacer con una tabla es borrar filas y modificar datos.
Desarrollaremos un pequeño programa que borre el artículo cuyo código sea el 1 y modifique el precio del artículo cuyo código sea 3.

"""
import psycopg2

conexion1=psycopg2.connect(database="bd1",user="postgres",password="66112233")
cursor1=conexion1.cursor()

cursor1.execute("delete from articulos where codigo=1")
cursor1.execute("update articulos set precio=50 where codigo=3")
conexion1.commit()

cursor1.execute("select codigo,descripcion,precio from articulos")

for fila in cursor1:
    print(fila)

conexion1.close()