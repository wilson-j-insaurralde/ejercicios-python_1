"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""
"""
Cómo se crean los Closures en Python
Para que se forme un closure, se deben cumplir tres condiciones:
- Debe haber una función anidada: Una función definida dentro de otra función.
- La función anidada debe hacer referencia a una variable del ámbito encerrador: Es decir, debe usar al menos una variable definida en la función externa.
- La función externa debe retornar la función anidada: En lugar de retornar un valor directamente, la función externa devuelve la definición de su función interna.
"""
def creador_saludos(idioma):
    if idioma=="es":
       prefijo = "hola"
    elif idioma=="en":
         prefijo ="hello"
    else:
         prefijo ="saludos"

    def generar_saludo(nombre):# Funcion anidada
          # 'prefijo' y 'nombre' son del ámbito encerrador y local, respectivamente
        return f"{prefijo}, {nombre}!" # Accede a 'prefijo' del ámbito E
    
    return generar_saludo # ¡Devolvemos la función anidada!

# Creamos una función anidada configurada para español
saludar_espanol = creador_saludos("es") 
# La función 'creador_saludo' ya terminó de ejecutarse,
# pero 'saludar_espanol' (la función interna) "recuerda" que 'prefijo' era "¡Hola"

print(saludar_espanol("Maria")) # Salida: ¡Hola, Maria!

# Creamos otra función anidada configurada para inglés
saludar_ingles = creador_saludos("en")
print(saludar_ingles("John")) # Salida: Hello, John!
    