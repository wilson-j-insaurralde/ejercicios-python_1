"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""


"""
Imagina que eres un programador y, con el tiempo, te encuentras escribiendo bloques de código que, aunque ligeramente distintos, cumplen funciones muy similares. Tal vez necesitas medir cuánto tiempo tarda en ejecutarse una función, o quizá quieres asegurarte de que un usuario esté autenticado antes de acceder a ciertas partes de tu aplicación. En cada caso, podrías copiar y pegar ese código auxiliar alrededor de tus funciones principales. Sin embargo, esta práctica, conocida como "copiar y pegar", es enemiga de la buena programación: introduce redundancia, dificulta el mantenimiento y es propensa a errores.

¿Qué son los decoradores y por qué son útiles?
En su esencia más simple, un decorador es una función que toma otra función como argumento, le añade alguna funcionalidad y luego devuelve esa nueva función (modificada o "decorada"). Piensa en ello como envolver un regalo: el regalo sigue siendo el mismo, pero el envoltorio le añade presentación, protección o un mensaje especial. De manera similar, los decoradores "envuelven" funciones, alterando o extendiendo su comportamiento sin modificar su código fuente original.

Este proceso de modificar el comportamiento de funciones o clases en tiempo de ejecución se conoce como metaprogramación. Los decoradores son una de las formas más accesibles y utilizadas de metaprogramación en Python, permitiéndonos escribir código más limpio, modular y reutilizable.

Ventajas
1 - Separación de intereses: Permiten separar el código que implementa la lógica de negocio de la función del código que implementa funcionalidades accesorias (logging, caché, validación, etc.).

2 - Reusabilidad: una vez que defines un decorador, puedes aplicarlo a múltiples funciones en diferentes partes de tu código sin tener que reescribir la lógica auxiliar.

3 - Legibilidad: la sintaxis especial de los decoradores (@) hace que sea muy claro a simple vista qué funcionalidades adicionales se están aplicando a una función.

4 - Mantenimiento: si necesitas cambiar cómo funciona una funcionalidad transversal (por ejemplo, cómo se registra el tiempo de ejecución), solo tienes que modificar el decorador en un solo lugar, y todos los lugares donde se use ese decorador se actualizarán automáticamente.

Problema 1
Creación de un decorador mínimo que muestre un mensaje antes y después de ejecutar la función principal.

"""

def mi_primer_decorador(func):
    """
    Este es un decorador básico que imprime un mensaje
    antes y después de la ejecución de la función.
    """
    def envoltura():
        print("antes de llamar a la funcion.")
        func() # Llama a la función original que fue pasada a 'mi_primer_decorador'
        print("Después de llamar a la función.")
    return envoltura # Retorna la función 'envoltura'

# Ahora, definimos una función y la "decoramos"
@mi_primer_decorador
def saludar():
    print("¡Hola desde la función saludar!")

# Llamamos a la función decorada
saludar()

print("--"*8)
@mi_primer_decorador
def saludar():
    print("tukii")
   
       
saludar()