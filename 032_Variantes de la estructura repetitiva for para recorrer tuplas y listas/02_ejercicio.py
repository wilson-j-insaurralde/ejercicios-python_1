"""
Almacenar en una lista de 5 elementos las tuplas con el nombre de empleado y su sueldo.
Implementar las funciones:
1) Carga de empleados.
2) Impresión de los empleados y sus sueldos.
3) Nombre del empleado con sueldo mayor.
4) Cantidad de empleados con sueldo menor a 1000.
"""

def carga():
    empleado=[]
    for x in range (5):
        em=input("ingrese el nombre del empleado: ")
        su=int(input("ingrese el sueldo del empleado: "))
        empleado.append((em,su))
    return (empleado)

def imprimir(lista):
    print("lista de empleados y sueldos: ")
    for em,su in lista:
        print(em,su,sep=" --- ")

def sueldo_mayor(lista):
    mayor=lista [0]
    for elemento in lista:
        if elemento[1]>mayor[1]:
            mayor=elemento
    print ("el empleado con mayor sueldo es: ", mayor[0]) 

def sueldosmenores(lista):
    cont=0
    for elemento in lista:
        if elemento[1]<1000:
            cont=cont+1
    print(f"la cantidad de empleados con sueldos menores a 1000 son : {cont}")

lista=carga()
imprimir(lista)
sueldo_mayor(lista)
sueldosmenores(lista)