"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Almacenar en una tupla los nombres de meses del año. Solicitar el ingreso del número de mes y mostrar seguidamente el nombre de dicho mes. Capturar la excepción IndexError.
"""


meses=("enero","febrero","marzo","abril","mayo","junio",
       "julio","agosto","septiembre","octubre","noviembre","diciembre")

try:
    me=int(input("ingrese el numero del mes deseado[1-12]: "))
    if me>0:
        print("el mes es: ",meses[me-1])
    else:
        print("En número de mes debe ir entre 1 y 12")
    

except IndexError:
    print("ingrese un numero de mes valido.")