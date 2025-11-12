#Ingresar un mail por teclado. Verificar si el string ingresado contiene solo un caracter "@".


mail=input("ingrese el mail: ")


cantidad =0
x=0

while x<len[mail]:
    if mail[x]=="@":
        cantidad=cantidad+1
    x=x+1
if cantidad==1:
    print("Contiene solo un caracter @ el mail ingresado")
else:
    print("Incorrecto")

"""Para analizar cada caracter del string ingresado disponemos una estructura while utilizando un contador llamado x que comienza con el valor cero y se repetirá tantas veces como caracteres tenga la cadena (mediante la función len obtenemos la cantidad de caracteres):

while x<len(mail):
Dentro del ciclo while verificamos cada caracter mediante un if y contamos la cantidad de caracterers "@":

    if mail[x]=="@":
        cantidad=cantidad+1
Cuando sale del ciclo while procedemos a verificar si el contador tiene almacenado el valor 1 y mostramos el mensaje respectivo:

if cantidad==1:
    print("Contiene solo un caracter @ el mail ingresado")
else:
    print("Incorrecto")
Los string en Python son inmutables, esto quiere decir que una vez que los inicializamos no podemos modificar su contenido:

nombre="juan"
nombre[0]="m" #esto no se puede"""

"""No hay que confundir cambiar parte del string con realizar la asignación de otro string a la misma variable, luego si es correcto asignar otro valor a un string:

nombre="juan"
print(nombre)
nombre="ana"
print(nombre"""

"""
Métodos propios de las cadenas de caracteres.
Los string tienen una serie de métodos (funciones aplicables solo a los string) que nos facilitan la creación de nuestros programas.

Los primeros tres métodos que veremos se llaman: lower, upper y capitalize.

upper() : devuelve una cadena de caracteres convertida todos sus caracteres a mayúsculas.
lower() : devuelve una cadena de caracteres convertida todos sus caracteres a minúsculas.
capitalize() : devuelve una cadena de caracteres convertida a mayúscula solo su primer caracter y todos los demás a minúsculas.
"""