"""
Crear un diccionario en Python para almacenar los datos de empleados de una empresa. La clave será su número de legajo y en su valor almacenar una lista con el nombre, profesión y sueldo.
Desarrollar las siguientes funciones:
1) Carga de datos de empleados.
2) Permitir modificar el sueldo de un empleado. Ingresamos su número de legajo para buscarlo.
3) Mostrar todos los datos de empleados que tienen una profesión de "analista de sistemas"
"""

def carga():    
    empleados={}
    seguir="s"
    while seguir=="s":
        legajo=int(input("ingrese el numero del legajo: "))
        nombre=input("ingrese el nombre del empleado")
        profesion=input("ingrese la profesion del empleado: ")
        sueldo=int(input("ingrese el sueldo del empleado: "))
        empleados[legajo]=[nombre,profesion,sueldo]
        seguir=input("desea ingresar otro legajo?[s/n]")
    return empleados
def modificarsueldo(empleados):
    legajo=int(input("ingrese el numero del legajo: "))
    if legajo in empleados:
        sueldo=int(input("ingrese el sueldo actualizado: "))
        empleados[legajo][2]=sueldo
def mostraranalistas(empleados):
    print("los empleados analistas en sistemas son: ")
    for toma in (empleados):
        if empleados[toma][1]=="analista de sistemas":
            print(toma,empleados[toma][0],empleados[toma][1],empleados[toma][2])
        
empleados= carga()
print("lista de empleados: ")
print(empleados)
modificarsueldo(empleados)
print("sueldos modificados: ")
print(empleados)
mostraranalistas(empleados)