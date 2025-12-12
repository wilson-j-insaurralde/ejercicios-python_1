"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Definir por asignación una lista con 8 elementos enteros. Contar cuantos de dichos valores almacenan un valor superior a 100.
"""

lista=[100,200,300,4,500,6,7,8]

cont=0
x=0
while x<len(lista):
    if lista[x]>100:
        cont=cont+1
    x=x+1
print (f"{cont} elementos almacenan un valor superior a 100")
