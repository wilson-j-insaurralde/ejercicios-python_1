"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Confeccionar un programa que almacene en un diccionario como clave el nombre de un contacto y como valor su número telefónico:
1) Carga de contactos y su número telefónico.
2) Pemitir modificar el número telefónico. Se ingresa el nombre del contacto para su búsqueda.
3) Imprimir la lista completa de contactos con sus números telefónicos.
"""
def carga():
    agenda={}
    seguir="s"
    while seguir=="s":
        nombre=input("ingrese el nombre: ")
        numero=int(input("ingrese el numero: "))
        agenda[nombre]=numero
        seguir=input("desea ingresar otro contacto?[s/n]")
    return agenda


def modificarnumero(agenda):
    nombre=input("ingrese el nombre del contacto: ")
    if nombre in agenda:
        num=int(input("ingrese el nuevo numero del contacto: "))
        agenda[nombre]=num
    else:
        print("no se encuentra dicha persona.")
        
def imprimir(agenda):
    print("lista de los contactos: ")
    for nombre in agenda:
        print(nombre,agenda[nombre])

agenda=carga()
modificarnumero(agenda)
imprimir(agenda)