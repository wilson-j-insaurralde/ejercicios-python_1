"""No todos los problemas pueden resolverse empleando estructuras secuenciales. Cuando hay que tomar una decisión aparecen las estructuras condicionales.
En nuestra vida diaria se nos presentan situaciones donde debemos decidir.
¿Elijo la carrera A o la carrera B?
¿Me pongo este pantalón?
Para ir al trabajo, ¿Elijo el camino A o el camino B?
Al cursar una carrera, ¿Elijo el turno mañana, tarde o noche?

Es común que en un problema se combinan estructuras secuenciales y condicionales."""

#Ingresar el sueldo de una persona, si supera los 3000 dolares mostrar un mensaje en pantalla indicando que debe abonar impuestos.

sueldo=int(input("ingrese el sueldo: "))
if (sueldo>3000) :
    print("sueldo mayor a 3000 dolares debe abonar impuestos")
else:
    print("no debe abonar impuestos")

"""Podemos observar lo siguiente: Siempre se hace la carga del sueldo, pero si el sueldo que ingresamos supera 3000 dolares se mostrará por pantalla el mensaje "Esta persona debe abonar impuestos", en caso que la persona cobre 3000 o menos no aparece nada por pantalla."""

"""
La palabra clave "if" indica que estamos en presencia de una estructura condicional; seguidamente disponemos la condición y finalizamos la línea con el caracter dos puntos.
La actividad dentro del if se indenta generalmente a 4 espacios.

Todo lo que se encuentre en la rama del verdadero del if se debe disponer a 4 espacios corrido a derecha.

La indentación es una característica obligatoria del lenguaje Python para codificación de las estructuras condicionales, de esta forma el intérprete de Python puede identificar donde finalizan las instrucciones contenidas en la rama verdadera del if.

Ejecutando el programa e ingresamos un sueldo superior a 3000. Podemos observar como aparece en pantalla el mensaje "Esta persona debe abonar impuestos", ya que la condición del if es verdadera
"""
