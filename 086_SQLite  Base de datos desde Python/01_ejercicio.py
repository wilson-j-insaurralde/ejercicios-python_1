"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
En principio no se requiere tener más que Python instalado para poder trabajar con SQLite. Podemos desde nuestra propia aplicación crear la base de datos y sus tablas.
"""

import sqlite3

conexion=sqlite3.connect("bd1.db")

try:
    conexion.execute("""
                    create table articulos(
                        codigo integer primary key autoincrement,
                        descripcion text,
                        precio real
                        )
                        """)
    print("se creo la tabla articulos")
except sqlite3.OperationalError:
    print("la tabla articulos ya existe")
conexion.close()
