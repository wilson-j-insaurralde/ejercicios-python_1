"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Se ingresa por teclado un valor entero, mostrar una leyenda que indique si el número es positivo, negativo o nulo (es decir cero)
"""
num=int(input("Ingrese un valor:"))
if num==0:
    print("Se ingresó el cero")
else:
    if num>0:
        print("Se ingresó un valor positivo")
    else:
        print("Se ingresó un valor negativo")