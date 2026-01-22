"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Problema 2
Crear una función que reciba una clave y retorne True si tiene al menos un número, una letra minúscula y una letra mayúscula. Definir 3 funciones anidadas que controlen cada uno de los tres casos.

"""


def validar_clave(clave):
    def tiene_minuscula():
        for caracter in clave:
            if caracter.islower():
                return True
        return False
    def tiene_mayuscula():
        for caracter in clave:
            if caracter.isupper():
                return True
        return False
    def tiene_numero():
        for caracter in clave:
            if caracter.isdigit():
                return True
        return False
    
    return tiene_minuscula() and tiene_mayuscula() and tiene_numero()

# --- Ejemplos de uso ---
print("--- Clave Válida ---")
clave1 = "MiClaveSegura123"
print(f"'{clave1}' es válida: {validar_clave(clave1)}") # Esperado: True
print("-" * 30)

print("\n--- Clave sin mayúscula ---")
clave2 = "miclavesegura123"
print(f"'{clave2}' es válida: {validar_clave(clave2)}") # Esperado: False
print("-" * 30)

print("\n--- Clave sin minúscula ---")
clave3 = "MICLAVESEGURA123"
print(f"'{clave3}' es válida: {validar_clave(clave3)}") # Esperado: False
print("-" * 30)

print("\n--- Clave sin número ---")
clave4 = "MiClaveSegura"
print(f"'{clave4}' es válida: {validar_clave(clave4)}") # Esperado: False
print("-" * 30)

print("\n--- Clave con solo minúsculas y números ---")
clave5 = "miclave123"
print(f"'{clave5}' es válida: {validar_clave(clave5)}") # Esperado: False
print("-" * 30)

print("\n--- Clave vacía ---")
clave6 = ""
print(f"'{clave6}' es válida: {validar_clave(clave6)}") # Esperado: False
print("-" * 30)

"""
Las 3 funciones internas 'tiene_minuscula', 'tiene_mayuscula' y 'tiene_numero' solo pueden ser invocadas desde dentro de la función 'validar_clave'.

Cada función anidada es una pequeña unidad de lógica que está intrínsecamente ligada a la validación de una clave dentro del contexto de 'validar_clave' y no tienen un propósito útil fuera de esta función, es por ello que se las dispone en forma local a la función principal.

Las funciones anidadas pueden acceder a los parámetros de la función principal y a sus variables locales, es decir en nuestro problema la función 'tiene_minuscula' puede acceder al parámetro llamado 'clave' definido en la función 'validar_clave'. Este acceso es una característica fundamental de las funciones anidadas.

Las funciones anidadas son útiles para organizar y modularizar el código dentro de una función más grande, manteniendo la limpieza y evitando la "contaminación" del espacio de nombres global.

Como ha quedado expuesto, la declaración de una función anidada es sorprendentemente sencilla y sigue la misma sintaxis que cualquier otra función en Python, con una única pero crucial diferencia: su definición ocurre dentro del cuerpo de otra función o método de una clase.
"""