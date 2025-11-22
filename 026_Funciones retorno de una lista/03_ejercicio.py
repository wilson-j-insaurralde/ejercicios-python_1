"""
Desarrollar un programa que permita cargar 5 nombres de personas y sus edades respectivas. Luego de realizar la carga por teclado de todos los datos imprimir los nombres de las personas mayores de edad (mayores o iguales a 18 años)
Imprimir la edad promedio de las personas.
"""
def mayores(nombre,edad):

    for x in range(len(edad)):
        if edad[x]>=18:
            print(nombre[x],"es mayor de edad")

def promedio(edad):
    suma=0
    for x in range (len(edad)):
        suma=suma+edad[x]
    promedio=(suma)/(len(edad))
    print(f"la edad promedio de la lista es: {promedio}")

def carga():
    edad=[]
    nombre=[]
    for x in range (5):
        nom=input("ingrese el nombre de la persona: ")
        ed=int(input("ingrese la edad de la persona: "))
        nombre.append(nom)
        edad.append(ed)
    
    return nombre,edad

nombre,edad=carga()
mayores(nombre,edad)
promedio(edad)