"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
En una empresa se almacenaron los sueldos de 10 personas.
Desarrollar las siguientes funciones y llamarlas desde el bloque principal:
1) Carga de los sueldos en una lista.
2) Impresión de todos los sueldos.
3) Cuántos tienen un sueldo superior a $4000.
4) Retornar el promedio de los sueldos.
5) Mostrar todos los sueldos que están por debajo del promedio.
"""
def promedioBajo(sueldo,promedio):
    
    print("sueldo por debajo del promedio: ")
    for x in range (len(sueldo)):
        if sueldo[x]<promedio:
            print(sueldo[x])
def promedio(sueldo):
    suma=0
    for x in range (len(sueldo)):
        suma=suma+sueldo[x]
    promedio= suma/(len(sueldo))
    print(f"el promedio de los sueldos es: {promedio}")
    return promedio


def superior(sueldo):
    sup=0
    for x in range (len(sueldo)):
        if sueldo[x]>4000:
            sup=sup+1
    print(f"{sup} poseen un sueldo superior a $4000")

def carga():
    sueldos=[]
    for x in range (10):
        su=int(input("ingrese el sueldo: "))
        sueldos.append(su)
    print("lista de sueldos: ")
    print(sueldos)    
    return sueldos

sueldo= carga()
superior(sueldo)
promediob=promedio(sueldo)
promedioBajo(sueldo,promediob)
