"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Confeccionar una función que reciba una palabra y verifique si es capicúa (es decir que se lee igual de izquierda a derecha que de derecha a izquierda)
"""
def cargarcapicua(cadena):
    indice=-1   
    iguales=0
    for x in range (0,(len(cadena)//2)):
        if (cadena[x]==cadena[indice]):
            iguales=iguales+1
        indice=indice-1
    print(cadena)
    if iguales==(len(cadena)//2):
        print("es capicua")
    else:
        print("no es capicua")


seguir="s"
while seguir=="s":
    palabra=input("ingrese la palabra: ")
    cargarcapicua(palabra)
    seguir=input("desea ingresar otra palabra?[s/n]")
    