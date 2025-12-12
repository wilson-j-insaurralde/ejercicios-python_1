"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Confeccionar un programa que permita cargar un código de producto como clave en un diccionario. Guardar para dicha clave el nombre del producto, su precio y cantidad en stock.
Implementar las siguientes actividades:
1) Carga de datos en el diccionario.
2) Listado completo de productos.
3) Consulta de un producto por su clave, mostrar el nombre, precio y stock.
4) Listado de todos los productos que tengan un stock con valor cero.
"""

def cargar():
    productos = {}
    seguir = "s"
    while seguir=="s":
        codigo=int(input("ingrese el codigo del producto: "))
        descripcion=(input("ingrese la descripcion del producto: "))
        precio=int(input("ingrese el precio del producto: "))
        stock=int(input("ingrese el stock: "))
        productos[codigo]=(descripcion,precio,stock)
        seguir=input("de sea seguir ingresando productos? [s/n]")

    return productos
def listacompleta(productos):
    print("lista de productos: ")
    for producto in productos:
        print (producto,productos[producto][0],productos[producto][1],productos[producto][2],sep=" --- ")
def consultaproducto(productos):
    ver=int(input("ingrese el codigo del producto a consultar: "))
    if ver in productos: 
        print("el producto es: ")
        print(ver,productos[ver][0],productos[ver][1],productos[ver][2], sep=" --- ")
def listado_stock_cero(productos):
    print("Listado de articulos con stock en cero:")
    for codigo in productos:
        if productos[codigo][2]==0:
            print(codigo,productos[codigo][0],productos[codigo][1],productos[codigo][2])

productos=cargar()
listacompleta(productos)
consultaproducto(productos)
listado_stock_cero(productos)