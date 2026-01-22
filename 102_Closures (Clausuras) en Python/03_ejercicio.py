"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""


def crear_contador(inicio=0):
    contador = inicio  # variable libre que la función interna "recuerda"
    
    def incrementar():
        nonlocal contador  # para modificar la variable del closure
        contador += 1
        return contador
    
    return incrementar


# Crear dos contadores independientes
contador_a = crear_contador(10)
contador_b = crear_contador(100)

print(contador_a())  # 11
print(contador_a())  # 12
print(contador_b())  # 101
print(contador_a())  # 13
print(contador_b())  # 102

"""
La palabra clave 'nonlocal' es obligatoria en Python, con esto le decimos que queremos acceder a la variable 'contador' definido en la función crear_contador, es decir en la función externa.

La función incrementar recuerda el estado de la variable contador incluso después de que crear_contador haya terminado.

Cada llamada a crear_contador genera un entorno independiente, por eso contador_a y contador_b no se mezclan.

Esto permite simular objetos con estado sin usar clases

"""