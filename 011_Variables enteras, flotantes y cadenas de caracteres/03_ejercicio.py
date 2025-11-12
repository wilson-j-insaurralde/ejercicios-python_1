"""
Realizar la carga de dos nombres por teclado. Mostrar cual de los dos es mayor alfabéticamente o si son iguales.
"""

nombre1=input("Ingrese el primer nombre:")
nombre2=input("Ingrese el segundo nombre:")
if nombre1==nombre2:
    print("Ingreso dos nombre iguales")
else:
    if nombre1>nombre2:
        print(nombre1)
        print("es mayor alfabeticamente")
    else:
        print(nombre2)
        print("es mayor alfabeticamente")

"""
 Cuando trabajamos con cadenas de caracteres al utilizar el operador > estamos verificando si una cadena es mayor alfabéticamente a otra (esto es distinto a cuando trabajamos con enteros o flotantes)

Por ejemplo 'luis' es mayor a 'carlos' porque la 'l' se encuentra más adelante en el abecedario que la c
 """       