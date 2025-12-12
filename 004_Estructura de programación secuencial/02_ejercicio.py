"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Problema:
Realizar la carga del precio de un producto y la cantidad a llevar. Mostrar cuanto se debe pagar (se ingresa un valor entero en el precio del producto)
"""

precio=int(input("ingrese el precio del producto: "))
cantidad= int (input("ingrese cantidad de productos: "))
monto= precio*cantidad 

print("el precio a pagar es: ",monto)
