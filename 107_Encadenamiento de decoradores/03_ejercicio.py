"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Problema 2
Definir dos decoradores con parámetros, uno que permita definir el rango de valores válidos y otro que haga un redondeo.
"""

def validar_rango(min_val, max_val):
    def decorador(func):
        def envoltura(*args, **kwargs):
            for arg in args:
                if not (arg >= min_val and arg <= max_val):
                    raise ValueError(f"Valor {arg} fuera del rango [{min_val}, {max_val}]")
            return func(*args, **kwargs)
        return envoltura
    return decorador

def redondear(decimales=2):
    def decorador(func):
        def envoltura(*args, **kwargs):
            resultado = func(*args, **kwargs)
            return round(resultado, decimales)
        return envoltura
    return decorador

@validar_rango(0, 100)   # primero valida que los valores estén en 0–100
@redondear(3)            # luego redondea el resultado a 3 decimales
def promedio(a, b):
    return (a + b) / 2

# Pruebas
print(promedio(50, 75))   #  válido ? 62.5
print(promedio(10, 20))   #  válido ? 15.0
print(promedio(150, 20))  #  lanza ValueError


"""
El decorador @redondear(3) envuelve primero promedio.

Luego @validar_rango(0, 100) envuelve todo lo anterior.

(El orden de escritura es inverso al orden de ejecución).
"""