"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""
"""
Cuando usamos decoradores, envolvemos una función con otra.
Esto tiene un efecto colateral: la función decorada pierde información importante como su nombre original (__name__) y su documentación (__doc__).

Esto puede traer problemas en:

Depuración: los errores mostrarán el nombre de la función envoltura en lugar del de la función real.
Documentación: herramientas como help() o pydoc mostrarán la docstring incorrecta.
Metaprogramación: si inspeccionamos funciones (con inspect), obtendremos datos erróneos.
Veamos con un ejemplo el problema:
"""
def mi_decorador(func):
    def envoltura(*args, **kwargs):
        """Función envoltorio sin docstring de la original"""
        print("Antes de la función...")
        resultado = func(*args, **kwargs)
        print("Después de la función...")
        return resultado
    return envoltura

@mi_decorador
def saludar():
    """Esta función imprime un saludo amigable."""
    print("¡Hola!")

print(saludar.__name__)  # envoltura 
print(saludar.__doc__)   # Función envoltorio sin docstring de la original