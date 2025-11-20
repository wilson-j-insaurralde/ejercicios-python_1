"""
Definir una lista y almacenar los nombres de 3 empleados.
Por otro lado definir otra lista y almacenar en cada elemento una sublista con los números de días del mes que el empleado faltó.
Imprimir los nombres de empleados y los días que faltó.
Mostrar los empleados con la cantidad de inasistencias.
Finalmente mostrar el nombre o los nombres de empleados que faltaron menos días. 

"""

empleados=[]
faltas=[]


for x in range(3):
    nom=input("ingrese el nombre del empleado: ")
    empleados.append(nom)
    cant=int(input("Cuantos dias falto:"))
    faltas[x].append([])
    
    
    for k in range (cant):
        cant2=int(input("ingrese el numero del dia que falto:"))
        faltas[x].append(cant2)

print("empleados y los dias que faltaron: ")

for x in range(3):
    print(empleados[x])
    for k in range(len(faltas[x])):
        print (faltas[x][k] )

men=len(faltas[0])
for x in range(1,3):
    if len(faltas[x])<men:
        men=len(faltas[x])

print("Empleado o empleados que faltaron menos")
for x in range(3):
    if len(faltas[x])==men:
           print(empleados[x])
