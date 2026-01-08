"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Definir una lista con 5 valores enteros. Mostrar los 5 valores formateados a derecha junto a su suma.
"""

lista=[2000,500,1700,24,7]
for elemento in lista:
    print(f" {elemento:10} ")

print("----------")    
print(f"{sum(lista):10}")