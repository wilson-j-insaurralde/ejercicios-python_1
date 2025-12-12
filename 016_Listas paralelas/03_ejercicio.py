"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
En un curso de 4 alumnos se registraron las notas de sus exámenes y se deben procesar de acuerdo a lo siguiente:
a) Ingresar nombre y nota de cada alumno (almacenar los datos en dos listas paralelas)
b) Realizar un listado que muestre los nombres, notas y condición del alumno. En la condición, colocar "Muy Bueno" si la nota es mayor o igual a 8, "Bueno" si la nota está entre 4 y 7, y colocar "Insuficiente" si la nota es inferior a 4.
c) Imprimir cuantos alumnos tienen la leyenda “Muy Bueno”.
"""

nombre=[]
nota=[]
estado=[]
insuficiente=0
muyBueno=0
bueno=0
for x in range(4):
    nom=input("ingrese el nombre del alumno: ")
    nt=int(input("ingrese la nota del alumno: "))
    nombre.append(nom)
    nota.append(nt)
    if nota[x]>=8:
        estado.append("muy bueno")
        muyBueno=muyBueno+1
    else: 
        if nota[x]>=4:
            estado.append("bueno")
            bueno=bueno+1
        else: 
            estado.append("insuficiente")
            insuficiente=insuficiente+1

for x in range(4):
    print(f"{nombre[x]} --- {nota[x]} --- {estado[x]} ")

print(f"muy buenos: {muyBueno}")
print(f"buenos:{bueno}")
print(f"insuficiente: {insuficiente}")