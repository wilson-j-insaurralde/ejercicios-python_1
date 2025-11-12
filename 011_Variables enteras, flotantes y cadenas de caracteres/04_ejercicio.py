"""
Realizar la carga de enteros por teclado. Preguntar después que ingresa el valor si desea cargar otro valor debiendo el operador ingresar la cadena 'si' o 'no' por teclado.
Mostrar la suma de los valores ingresados.
"""

opcion="si"
suma=0
while opcion=="si":
    valor=int(input("Ingrese un valor:"))
    suma=suma+valor
    opcion=input("Desea cargar otro numero (si/no):")
print("La suma de valores ingresados es")
print(suma)

"""
Para resolver este problema hemos inicializado una variable de tipo cadena de caracteres (también se las llama variables de tipo string) con el valor "si", esto hace que la condición del while se verifique verdadera la primera vez. Dentro del while luego de cargar el valor entero se pide la carga por teclado que confirme si desea cargar otro valor, en caso que cargue el string "si" el ciclo repetitivo while se vuelve a repetir.

El ciclo se corta cuando el operador carga un string distinto a "si".

Es importante notar que el string "si" es distinto al string "Si", es decir las mayúsculas no tienen el mismo valor alfabético que las minúsculas (después veremos que podemos convertir mayúsculas a minúsculas y viceversa)
"""