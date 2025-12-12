"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Realizar la carga de dos nombres de personas distintos. Mostrar por pantalla luego ordenados en forma alfabética.
"""


nombre1=input("Ingrese el primer nombre:")
nombre2=input("Ingrese el segundo nombre:")
print("Listado alfabetico:")
if nombre1<nombre2:
    print(nombre1)
    print(nombre2)
else:
    print(nombre2)
    print(nombre1)