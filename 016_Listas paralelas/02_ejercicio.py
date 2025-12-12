"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Crear y cargar dos listas con los nombres de 5 productos en una y sus respectivos precios en otra. Definir dos listas paralelas. Mostrar cuantos productos tienen un precio mayor al primer producto ingresado.
"""

nombre=[]
precios=[]

for x in range(5):
    producto=input("ingrese el nombre del producto: ")
    nombre.append(producto)
    pe=int(input("ingrese el precio del producto"))
    precios.append(precios)
cantidad=0
for x in range(1,5):
    print ("los productos que tienen mayor precio que el primero ingresado son: ")
    if precios[x]>precios[0]:
        print(f"{nombre[x]}---{precios[x]}")
        cantidad=cantidad+1
      
print("Cantidad de productos con un precio mayor al primer producto ingresado")
print(cantidad)