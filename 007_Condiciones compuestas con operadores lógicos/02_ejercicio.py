"""
Operador or
Traducido se lo lee como “O”. Si la condición 1 es Verdadera o la condición 2 es Verdadera, luego ejecutar la rama del Verdadero.
Cuando vinculamos dos o más condiciones con el operador “or", con que una de las dos condiciones sea Verdadera alcanza para que el resultado de la condición compuesta sea Verdadero.
"""

"""
Problema:
Se carga una fecha (día, mes y año) por teclado. Mostrar un mensaje si corresponde al primer trimestre del año (enero, febrero o marzo) Cargar por teclado el valor numérico del día, mes y año.
Ejemplo: dia:10 mes:2 año:2018
La carga de una fecha se hace por partes, ingresamos las variables dia, mes y año.
Mostramos el mensaje "Corresponde al primer trimestre" en caso que el mes ingresado por teclado sea igual a 1, 2 ó 3.
En la condición no participan las variables dia y año.
"""

dia=int(input("Ingrese nro de día:"))
mes=int(input("Ingrese nro de mes:"))
año=int(input("Ingrese nro de año:"))
if mes==1 or mes==2 or mes==3:
    print("Corresponde al primer trimestre")
