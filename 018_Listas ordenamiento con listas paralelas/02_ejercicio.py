"""
Crear y cargar en un lista los nombres de 5 países y en otra lista paralela la cantidad de habitantes del mismo. Ordenar alfabéticamente e imprimir los resultados. Por último ordenar con respecto a la cantidad de habitantes (de mayor a menor) e imprimir nuevamente.
"""

paises=[]
habitantes=[]

for x in range (5):
    pa=input("ingrese el pais: ")
    paises.append(pa)
    ha=float(input("ingrese el numero de habitantes: "))
    habitantes.append(ha)

aux1=0
aux2=0
for k in range(5):
    for x in range (4-k):
        if (habitantes[x]<habitantes[x+1]):
            aux1=habitantes[x]
            habitantes[x]=habitantes[x+1]
            habitantes[x+1]=aux1
            aux2=paises[x]
            paises[x]=paises[x+1]
            paises[x+1]=aux2

print("ordenados por cantidad de habitantes: ")

for x in range(5):
    print (f"{paises[x]} --- {habitantes[x]}")
aux1=0
aux2=0
for k in range(5):
    for x in range(4-k):
        if (paises[x]>paises[x+1]):
            aux1=paises[x]
            paises[x]=paises[x+1]
            paises[x+1]=aux1
            aux2=habitantes[x]
            habitantes[x]=habitantes[x+1]
            habitantes[x+1]=aux2

print ("ordenado alfabeticamente: ")
for x in range(5):
    print (f"{paises[x]} --- {habitantes[x]}")










