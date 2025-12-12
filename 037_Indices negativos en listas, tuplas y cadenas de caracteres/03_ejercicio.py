"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Cargar una cadena de caracteres por teclado. Mostrar la cadena del final al principio utilizando subíndices negativos.
"""
def mostraralreves(cadena):
    
    indice=-1
    for x in range(len(cadena)):
        
        print(cadena[indice],end="")
        indice=indice-1
    print("")
seguir="s"
while seguir=="s":
    cadena=input("ingrese la cadena de caracteres: ")
    mostraralreves(cadena)
    seguir=input("desea ingresar otra palabra?[s/n]")
    
