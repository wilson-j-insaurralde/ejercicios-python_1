"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""


"""
Cuando insertamos una fila en una tabla que contiene un campo que se auto incrementa podemos recuperar dicho valor en el mismo momento que efectuamos la inserción.
"""

import mysql.connector 

conexion1=mysql.connector.connect(host="localhost",user="root",passwd="",database="bd1")

cursor1=conexion1.cursor()
sql="insert into articulos (descripcion, precio) values (%s,%s)"
datos=("naranja",23.50)
cursor1.execute(sql,datos)
conexion1.commit()
print("valor del ultimo codigo de articulo generado: ",cursor1.lastrowid)
conexion1.close()