"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Controlar que el "XAMPP Control Panel" se encuentre en ejecución el servidor de MySQL:

El primer programa que implementaremos nos conectaremos con el servidor de MySQL y mostraremos todas las bases de datos existentes (una de esas debería ser bd1)
"""
#Paquete de Python necesario para conectarnos a MySQL
#  pip install mysql-connector 


import mysql.connector

conexion1=mysql.connector.connect(host="localhost",user="root",passwd="")
cursor1=conexion1.cursor()
cursor1.execute("show databases")
for base in cursor1:
    print(base)
conexion1.close()
