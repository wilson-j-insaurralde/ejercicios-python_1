"""Inicializar un string con la cadena "mAriA" luego llamar a sus métodos upper(), lower() y capitalize(), guardar los datos retornados en otros string y mostrarlos por pantalla."""

nombre1="mAriA"
print(nombre1)
nombre2=nombre1.upper()
print(nombre2)
nombre3=nombre1.lower()
print(nombre3)
nombre4=nombre1.capitalize()
print(nombre4)

"""
Para llamar a un método del string debemos disponer entre el nombre del string y el método el caracter punto:

nombre2=nombre1.upper()
Es importante decir que el string nombre1 no se modifica su contenido (recordar que un string es inmutable) pero el método upper() retorna el contenido de la variable nombre1 pera convertida a mayúsculas. El dato devuelto se almacena en la variable nombre2.
"""