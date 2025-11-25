"""
Definir una función que cargue una lista con palabras y la retorne.
Luego otra función tiene que mostrar todas las palabras de la lista que tienen más de 5 caracteres.
"""

def carga():
    lista=[]
    n=int(input("ingrese la cantidad de palabras: "))
    for x in range (n):
        pa=input("ingrese la palabras: ")
        lista.append(pa)
    return lista
def moostrar(palabras):
    print("Palabras ingresadas con mas de 5 caracteres")
    for palabra in palabras:
        if len(palabra)>5:
            print(palabra)


lista= carga()
moostrar(lista)