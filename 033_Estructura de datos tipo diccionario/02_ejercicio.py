"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Crear un diccionario que permita almacenar 5 artículos, utilizar como clave el nombre de productos y como valor el precio del mismo.
Desarrollar además las funciones de:
1) Imprimir en forma completa el diccionario
2) Imprimir solo los artículos con precio superior a 100.
"""

def cargar ():
    tuki={}
    for x in range (5):
        clave=input("ingrese el nombre del producto: ")
        valor=int(input("ingrese el precio del producto: "))
        tuki[clave]=valor
    return tuki

def imprimir(dicionarrio):
    print("lista de productos")
    for clave in dicionarrio:
        print(clave,dicionarrio[clave])

def imprimirpreciomayor100(productos):
    print("porductos con precios mayor a 100")
    for nombre in productos:
        if productos[nombre]>100:
            print(nombre)


productos=cargar()
imprimir(productos)
imprimirpreciomayor100(productos)