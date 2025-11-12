"""
Hasta este momento hemos visto como definir variables enteras y flotantes. Realizar su carga por asignación y por teclado.

Para iniciarlas por asignación utilizamos el operador =
#definición de una variable entera
cantidad=20
#definición de una variable flotante
altura=1.92
Como vemos el intérprete de Python diferencia una variable flotante de una variable entera por la presencia del caracter punto.

Para realizar la carga por teclado utilizando la función input debemos llamar a la función int o float para convertir el dato devuelto por input:

cantidad=int(input("Ingresar la cantidad de personas:"))
altura=float(input("Ingresar la altura de la persona en metros ej:1.70:"))
A estos dos tipos de datos fundamentales (int y float) se suma un tipo de dato muy utilizado que son las cadenas de caracteres.

Una cadena de caracteres está compuesta por uno o más caracteres. También podemos iniciar una cadena de caracteres por asignación o ingresarla por teclado.

Inicialización de una cadena por asignación:

#definición e inicio de una cadena de caracteres
dia="lunes"
Igual resultado obtenemos si utilizamos la comilla simple:

#definición e inicio de una cadena de caracteres
dia='lunes'
Para la carga por teclado de una cadena de caracteres utilizamos la función input que retorna una cadena de caracteres:

nombre=input("ingrese su nombre:")

"""