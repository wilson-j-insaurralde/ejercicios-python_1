"""
Almacenar en una lista los sueldos (valores float) de 5 operarios. Imprimir la lista y el promedio de sueldos
"""

list=[]
suma=0
for x in range(5):
    sueldo=float(input("ingrese el sueldo: "))
    list.append(sueldo)
    suma=suma+sueldo

promedio=suma/5

print(f"lista de los sueldos: {list}")
print(f"el promedio de los sueldos es: {promedio}")