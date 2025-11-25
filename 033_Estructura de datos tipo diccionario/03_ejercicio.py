"""
Desarrollar una aplicación que nos permita crear un diccionario ingles/castellano. La clave es la palabra en ingles y el valor es la palabra en castellano.
Crear las siguientes funciones:
1) Cargar el diccionario.
2) Listado completo del diccionario.
3) Ingresar por teclado una palabra en ingles y si existe en el diccionario mostrar su traducción.
"""
def cargar():
    diccionario={}
    n=int(input("ingrese el numero de palabras: "))
    for x in range(n):
        palabra=input("ingrese la palabra: ")
        traduccion=input("ingrese su traduccion: ")
        diccionario[palabra]=traduccion
    return diccionario
"""
def cargar():
    diccionario={}
    continua="s"
    while continua=="s":
        caste=input("Ingrese palabra en castellano:")
        ing=input("Ingrese palabra en ingles:")
        diccionario[ing]=caste
        continua=input("Quiere cargar otra palabra:[s/n]")
    return diccionario
"""

def imprimirtodo(diccionario):
    print("listado completo del diccionario: ")
    for palabra in diccionario:
        print(palabra,diccionario[palabra], sep=" --- ")
def consultapalabra(diccionario):
        
        pal=input("ingrese la palabra a consultar: ")
        if pal in diccionario:
            print ("su traduccion es: ",diccionario[pal])




diccionario=cargar()
imprimirtodo(diccionario)
consultapalabra(diccionario)
