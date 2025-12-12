"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Confeccionar una función que reciba entre 2 y 5 enteros. La misma nos debe retornar la suma de dichos valores. Debe tener tres parámetros por defecto.
"""
def sumar(v1,v2,v3=0,v4=0,v5=0):#si no ingresa un valor deja por defecto 0
    s=v1+v2+v3+v4+v5
    return s




print("La suma de 5 + 6")
print(sumar(5,6))
print("La suma de 1 + 2 + 3")
print(sumar(1,2,3))
print("La suma de 1 + 2 + 3 + 4 + 5")
x=sumar(1,2,3,4,5)
print(x)
