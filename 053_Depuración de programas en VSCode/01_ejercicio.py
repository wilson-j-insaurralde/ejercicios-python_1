"""Abriremos algún programa que hemos desarrollado para ver como podemos depurarlo."""

lista=[10,7,3,7,2]
suma=0
x=0
while x<len(lista):
    suma=suma+lista[x]
    x=x+1
print("Los elementos de la lista son")
print(lista)
print("La suma de todos sus elementos es")    
print(suma) 
"""
Procederemos ahora a abrir la opción de "Depurar" ( Ctrl + Shift + D o el ícono de la barra de actividades) e iniciamos la depuración.
"""
"""
Como vemos aparece una barra de botones que nos permite:

Continuar (F5) (el triángulo verde)
Depurar paso a paso por procedimiento (F10)
Depurar paso a paso por instrucciones (F11)
Salir de depuración (Shift + F11)
Reiniciar (Ctrl + Shift + F5)
Detener (Shift+F5)
"""
