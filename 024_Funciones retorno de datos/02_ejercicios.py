"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Confeccionar una función que le enviemos como parámetros dos enteros y nos retorne el mayor.
"""
def mayor(x,y):
    if x>y:
        return x
    else: return y

num1=int(input("ingrese el primer numero: "))
num2=int(input("ingrese el segundo numero: "))

print(f"el numero mayor es: ",mayor(num1,num2))