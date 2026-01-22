"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""


def crear_sistema_puntuacion():
    puntuacion = 0
    historial = []

    def sistema(accion, valor=0):
        nonlocal puntuacion, historial
        if accion == "sumar":
            puntuacion += valor
            historial.append(("sumar", valor))
        elif accion == "restar":
            puntuacion -= valor
            historial.append(("restar", valor))
        elif accion == "mostrar":
            return puntuacion
        elif accion == "historial":
            return historial
        else:
            return "Acción no válida"
        return puntuacion

    return sistema


# Crear el sistema
puntos = crear_sistema_puntuacion()

print(puntos("sumar", 10))      # 10
print(puntos("sumar", 20))      # 30
print(puntos("restar", 5))      # 25
print("Puntuación actual:", puntos("mostrar"))  # 25
print("Historial:", puntos("historial"))  
# [('sumar', 10), ('sumar', 20), ('restar', 5)]


"""
El closure mantiene el estado de la puntuación y el historial sin usar clases.
Puede crear múltiples sistemas de puntuación independientes para distintos jugadores.
Es escalable: podrías añadir multiplicadores, combos, bonus sin cambiar la idea base.
"""