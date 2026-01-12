"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Definir una función de orden superior llamada operar. Llegan como parámetro dos enteros y una función. En el bloque de la función llamar a la función que llega como parámetro y enviar los dos primeros parámetros.
La función retorna un entero.
"""

def operar(v1,v2,fn):
    return fn(v1,v2)

def sumar (v1,v2):
    return v1+v2
def restar (v1,v2):
    return v1-v2
def multiplicar(v1,v2):
    return v1*v2
def dividir(v1,v2):
    return v1/v2


resultado1=operar(3,5,sumar)
print(resultado1)

resultado2=operar(3,5,restar)
print(resultado2)

resultado3=operar(3,5,multiplicar)
print(resultado3)

resultado4=operar(3,5,dividir)
print(resultado4)

print(operar(4,4,sumar))