"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Desarrollar una función que solicite la carga del dia, mes y año y almacene dichos datos en una tupla que luego debe retornar. La segunda función a implementar debe recibir una tupla con la fecha y mostrarla por pantalla.
"""

def carga():
    dia=int(input("ingrese el numero del dia: "))
    mes=int(input("ingrese el numero del mes: "))
    agno=int(input("ingrese el año: "))

    return (dia,mes,agno)

def imprimir(tupla):

    print(tupla[0],tupla[1],tupla[2],sep="/")

tuplina=carga()
imprimir(tuplina)