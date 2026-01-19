"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""


"""instalar: 
pip install psycopg2"""

"""
El primer programa que implementaremos nos conectaremos con el servidor de PostgreSQL e insertaremos un par de filas en la tabla 'articulos' que creamos desde el programa 'pgAdmin'.
"""

import psycopg2

conexion1 = psycopg2.connect(database="bd1", user="postgres", password="66112233")
cursor1=conexion1.cursor()
sql="insert into articulos(descripcion, precio) values (%s,%s)"
datos=("naranjas", 23.50)
cursor1.execute(sql, datos)
datos=("peras", 34)
cursor1.execute(sql, datos)
datos=("bananas", 25)
cursor1.execute(sql, datos)
conexion1.commit()
conexion1.close() 