"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Problemas propuestos
Se desea saber la temperatura media trimestral de cuatro paises. Para ello se tiene como dato las temperaturas medias mensuales de dichos paises.
Se debe ingresar el nombre del país y seguidamente las tres temperaturas medias mensuales.
Seleccionar las estructuras de datos adecuadas para el almacenamiento de los datos en memoria.
a - Cargar por teclado los nombres de los paises y las temperaturas medias mensuales.
b - Imprimir los nombres de las paises y las temperaturas medias mensuales de las mismas.
c - Calcular la temperatura media trimestral de cada país.
c - Imprimir los nombres de los paises y las temperaturas medias trimestrales.
b - Imprimir el nombre del pais con la temperatura media trimestral mayor.
"""
paises=[]
tempMediaMensual=[]
tempmediatrimestral=[]

for x in range (4):
    pa=input("ingrese el pais: ")
    paises.append(pa)
    temp1=float(input("ingrese la primera temperatura: "))
    temp2=float(input("ingrese la segunda temperatura: "))
    temp3=float(input("ingrese la tercera temperatura: "))
    tempMediaMensual.append([temp1,temp2,temp3])
print("Paises y temperaturas medias de los ultimos tres meses mensuales")
for x in range (4):
        print (f" {paises[x]} --- {tempMediaMensual[x][0]} --- {tempMediaMensual[x][1]} --- {tempMediaMensual[x][2]}\n ")
suma=0

for x in range (4):
      
      suma= tempMediaMensual[x][0]+ tempMediaMensual [x][1] + tempMediaMensual[x][2]
      promedio=suma/3
      tempmediatrimestral.append(promedio)

print("pisesy temperatura media trimestral")

for x in range (4):
        print (f" {paises[x]} --- {tempmediatrimestral[x]}\n ")

mayor=0
for x in range (1,4):
       if tempmediatrimestral[x]>tempmediatrimestral[mayor]:
              mayor=x

print (f"el pais con mayor temperatura es : {paises[mayor]}")
