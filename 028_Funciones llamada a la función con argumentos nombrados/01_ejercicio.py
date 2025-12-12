"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Confeccionar una función que reciba el nombre de un operario, el pago por hora y la cantidad de horas trabajadas. Debe mostrar su sueldo y el nombre. Hacer la llamada de la función mediante argumentos nombrados.
"""
def calcular (nombre,cantidadhoras,costohora):
    sueldo= cantidadhoras*costohora
    print(f"{nombre} el sueldo a pagar es {sueldo}")

calcular("pedro",10,5)
calcular(cantidadhoras=80,nombre="negro",costohora=0.5)
calcular(costohora=3,cantidadhoras=8,nombre="negrosqui")




#print("uno",end="-") print por de fecto tiene asignado "/n" (salto de linea) con el parametro "end=" le podemos poner otro. como por ejemplo un guion  