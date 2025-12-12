"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Confeccionar una función que le enviemos como parámetro un string y nos retorne la cantidad de caracteres que tiene. En el bloque principal solicitar la carga de dos nombres por teclado y llamar a la función dos veces. Imprimir en el bloque principal cual de las dos palabras tiene más caracteres.
"""

def cantidad(cant):
    cantidad=len(cant)
    return cantidad

nom1=str(input("ingrese el primer string: "))
nom2=str(input("ingrese el segundo string: "))
x=cantidad(nom1)
y=cantidad(nom2)
if x==y:
    print(f"{nom1} y {nom2} poseen la misma cantidad de caracteres.")
else:
    if x>y:
        print(F"{nom1} pose mas caracteres")
    else: 
        print(f"{nom2} posee mas caracteres")