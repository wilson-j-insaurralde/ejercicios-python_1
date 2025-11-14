"""
Cargar por teclado y almacenar en una lista las alturas de 5 personas (valores float)
Obtener el promedio de las mismas. Contar cuántas personas son más altas que el promedio y cuántas más bajas.
"""

list=[]

altas=0
bajas=0
suma=0

for x in range(5):
    altura=float(input("ingrese la altura: "))
    list.append(altura)
    suma=suma+altura

promedio=suma/5

for x in range(5):
    if list[x]>promedio:
        altas=altas+1
    else :
        bajas=bajas+1

print(f"lista de alturas: {list}")
print(f"promedio de altura: {promedio}")
print(f"mas altas que el promedio: {altas}")
print(f"mas bajas que el promedio: {bajas}")