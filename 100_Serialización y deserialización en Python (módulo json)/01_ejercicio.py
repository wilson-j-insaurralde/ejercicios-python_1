"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Definiciones básicas.
Serialización: Consiste en convertir un objeto de Python (normalmente una lista o diccionario) en un string.
Deserialización: Consiste en convertir un string en un objeto de Python (normalmente una lista o diccionario).
Como vemos son los dos caminos posibles para transformar una estructura de datos en otra estructura.

Problema 1
Definir un string en Python con la estructura interna de un archivo JSON.
Deserializar el string y convertirlo a una lista de Python. Luego volver a serializar la lista a un string.

"""

import json

cadena1="""
  [
      {
          "codigo":"1",
          "descripcion":"papas",
          "precio":"12"
      },
      {
          "codigo":"2",
          "descripcion":"naranjas",
          "precio":"25"
      }
  ]
"""
print(type(cadena1))
print(cadena1)
print("_"*80)
lista=json.loads(cadena1)
print(type(lista))
print(lista)
print("_"*80)
cadena2=json.dumps(lista)
print(type(cadena2))
print(cadena2)



"""
Transformación de datos entre Python y JSON
Los tipos de datos en JSON son muy similares a los tipos de datos en Python, pero no son exactamente iguales.
La conversión en los procesos de serializar y deserializar son:

Python	            JSON
dic	                object
list o tupla    	array
str	                string
int y float	        number
True	            true
False	            false
None	            null

"""