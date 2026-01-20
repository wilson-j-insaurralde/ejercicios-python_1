import psycopg2

class tuki:
    def abrir(self):
        conexion1=psycopg2.connect(database="bd1", user="postgres", password="66112233")
        return conexion1

    def carga(self,datos):
        cone=self.abrir()
        try:
            cursor=cone.cursor()
            sql="insert into articulos (descripcion,precio) values (%s,%s)"
            cursor.execute(sql,datos)
            cone.commit()
        finally:
            cone.close()

    def consultar(self,datos):
        cone=self.abrir()
        try:
            cursor=cone.cursor()
            sql="select descripcion,precio from articulos where codigo=%s"
            cursor.execute(sql,datos)
            return cursor.fetchall()
        finally:
            cone.close()
    def recuperar_todos(self):
        cone=self.abrir()
        try:
            cursor=cone.cursor()
            sql="select codigo,descripcion,precio from articulos"
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            cone.close()
    
    def baja(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="delete from articulos where codigo=%s"
        cursor.execute(sql, datos)
        cone.commit()
        return cursor.rowcount # retornamos la cantidad de filas borradas

    def modificacion(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="update articulos set descripcion=%s, precio=%s where codigo=%s"
        cursor.execute(sql, datos)
        cone.commit()
        return cursor.rowcount # retornamos la cantidad de filas modificadas