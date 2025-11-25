"""
Crear un diccionario en Python que defina como clave el número de documento de una persona y como valor un string con su nombre.
Desarrollar las siguientes funciones:
1) Cargar por teclado los datos de 4 personas.
2) Listado completo del diccionario.
3) Consulta del nombre de una persona ingresando su número de documento.
"""
def cargar():
    agenda={}
    for x in range(4):
        nombre=input("ingrese el nombre de la persona: ")
        documento=int(input("ingrese el documento:"))
        agenda[documento]=nombre

    return agenda

def imprimir(agenda):
    print("listado completo de la agenda: ")    
    for documento in agenda:
        print (documento,agenda[documento],sep=" --- ")
def consulta(agenda):
    con=int(input("ingrese el documento que desea consultar: "))
    if con in agenda: 
        print("el nombre es: ",agenda[con])
    else: 
        print("no se encuentra.")
agenda=cargar()
imprimir(agenda)
consulta(agenda)
