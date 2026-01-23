"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

# Otro ejemplo básico de Closure

def hacer_multiplicador(factor):
    # 'factor' es una variable del ámbito encerrador para 'multiplicar_por_factor'

    def multiplicar_por_factor(numero): # Función anidada
        # Accede a 'factor' del ámbito encerrador
        return numero * factor
    
    return multiplicar_por_factor # La función externa devuelve la función anidada (closure)

# Creamos dos closures diferentes
duplicador = hacer_multiplicador(2) # 'duplicador' es un closure que "recuerda" factor = 2
triplicador = hacer_multiplicador(3) # 'triplicador' es un closure que "recuerda" factor = 3

print(f"Duplicar 5: {duplicador(5)}")   # Salida: Duplicar 5: 10
print(f"Triplicar 5: {triplicador(5)}") # Salida: Triplicar 5: 15

# Observa que 'hacer_multiplicador' ya terminó de ejecutarse,
# pero 'duplicador' y 'triplicador' siguen usando su 'factor' recordado.