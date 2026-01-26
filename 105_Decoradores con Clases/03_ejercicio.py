"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""


"""
Problema 3
Implementar un decorador de clase con argumentos.
"""

class DecoradorParametrizado:
    def __init__(self, mensaje):
        self.mensaje = mensaje  # Guardamos el parámetro del decorador

    def __call__(self, func):
        # Aquí definimos la función envoltura
        def envoltura(*args, **kwargs):
            print(F"{self.mensaje} - Antes de la funcion")
            resultado=func(*args,**kwargs)
            print(f"{self.mensaje} - Después de la función")
            return resultado
        return envoltura
# Uso del decorador con parámetro
@DecoradorParametrizado("Depuración")
def principal():
    print("Función principal ejecutándose.")

# Llamada
principal()