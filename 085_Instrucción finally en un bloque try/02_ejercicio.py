"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Conectarse a una base de datos de MySQL y ejecutar un comando SQL incorrecto
"""
import mysql.connector

try:
    conenexion1=mysql.connector.connect(host="localhost",user="root",password="")
    cursor1=conenexion1.cursor()
    cursor1.execute("show databasesqqqqq")
    for bases in cursor1:
        print(bases)


except  mysql.connector.errors.ProgrammingError:
    print("error en comandos sql")
finally:
    conenexion1.close()
    print("se cerro la conexion a la base de datos")