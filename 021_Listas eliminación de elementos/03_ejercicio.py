"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Problemas propuestos
Crear dos listas paralelas. En la primera ingresar los nombres de empleados y en la segunda los sueldos de cada empleado.
Ingresar por teclado cuando inicia el programa la cantidad de empleados de la empresa.
Borrar luego todos los empleados que tienen un sueldo mayor a 10000 (tanto el sueldo como su nombre)
"""

empleados=[]
sueldo=[]
n=int(input("ingrese la cantidad de empleados: "))

for x in range(n):
    nombre=input("ingrese el nombre del empleado: ")
    empleados.append(nombre)
    su=float(input("ingrese el sueldo del empledo: "))
    sueldo.append(su)

for x in range(n):
    print(f"{empleados[x]} --- {sueldo[x]}")

posicion=0
while posicion<len(sueldo):

    if sueldo[posicion]>1000:
        sueldo.pop(posicion)
        empleados.pop(posicion)
    else: 
        posicion=posicion+1

for x in range(len(sueldo)):
    print(f"{empleados[x]} --- {sueldo[x]}")
