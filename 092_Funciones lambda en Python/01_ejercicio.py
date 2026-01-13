"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Definir una función de orden superior llamada operar. Llegan como parámetro dos enteros y una función. En el bloque de la función llamar a la función que llega como parámetro y enviar los dos primeros parámetros.
Desde el bloque principal llamar a operar y enviar distintas expresiones lambdas que permitan sumar, restar, multiplicar y dividir.
"""
def operar(v1,v2,fn):
    return fn(v1,v2)

resultado=operar(4,5,lambda x1,x2: x1+x2)
print(resultado)

resultad2=operar(5,5,lambda x1,x2:x1*x2)
print(resultad2)

print(operar(10,25,lambda x1,x2: x1*x2))

print(operar(10,25,lambda x1,x2: x1/x2))
