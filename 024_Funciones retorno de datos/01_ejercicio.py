"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Confeccionar una función que le enviemos como parámetro el valor del lado de un cuadrado y nos retorne su superficie.
"""
def superficie(lado):
    superficie=lado*lado
    return superficie

num=int(input("ingrese el lado del cuadrado: "))
superficie=superficie(num)
print(f"la superficie del cuadrado es: {superficie}")


"""
Aparece una nueva palabra clave en Python para indicar el valor devuelto por la función: return

La función retornar_superficie recibe un parámetro llamado lado, definimos una variable local llamada sup donde almacenamos el producto del parámetro lado por sí mismo.

La variable local sup es la que retorna la función mediante la palabra clave return:

def retornar_superficie(lado):
    sup=lado*lado
    return sup
Hay que tener en cuenta que las variables locales (en este caso sup) solo se pueden consultar y modificar dentro de la función donde se las define, no se tienen acceso a las mismas en el bloque principal del programa o dentro de otra función.

Hay un cambio importante cuando llamamos o invocamos a una función que devuelve un dato:

superficie=retornar_superficie(va)
Es decir el valor devuelto por la función retornar_superficie se almacena en la variable superficie.

Es un error lógico llamar a la función retornar_superficie y no asignar el valor a una variable:

retornar_superficie(va)
El dato devuelto (en nuestro caso la superficie del cuadrado) no se almacena.

Si podemos utilizar el valor devuelto para pasarlo a otra función:

va=int(input("Ingrese el valor del lado del cuafrado:"))
print("La superficie del cuadrado es",retornar_superficie(va))
La función retornar_superficie devuelve un entero y se lo pasamos a la función print para que lo muestre.
"""