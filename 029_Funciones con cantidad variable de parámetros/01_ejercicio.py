"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Confeccionar una función que reciba entre 2 y n (siendo n = 2,3,4,5,6 etc.) valores enteros, retornar la suma de dichos parámetros.
"""
def sumar(num1,num2,*lista):
    suma=num1+num2
    for x in range (len(lista)):
        suma=suma+lista[x]      

    return suma
print(sumar(2,2))
print(sumar(1,2,3,4,5))
print(sumar(1,2,3,4,5,6,7,8,9,10,11))