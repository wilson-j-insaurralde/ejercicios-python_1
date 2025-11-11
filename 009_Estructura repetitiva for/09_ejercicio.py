"""
Problemas propuestos
Ha llegado nuevamente la parte fundamental, que es el momento donde uno desarrolla individualmente un algoritmo para la resolución de un problema.

Confeccionar un programa que lea n pares de datos, cada par de datos corresponde a la medida de la base y la altura de un triángulo. El programa deberá informar:
a) De cada triángulo la medida de su base, su altura y su superficie.
b) La cantidad de triángulos cuya superficie es mayor a 12.
"""

n=int(input("ingrese la cantidad de triangulos: "))
mayor=0
for x in range(n):
    base=int(input("ingrese su base: "))
    altura=int(input("ingrese su altura: "))
    superficie=base*altura
    print(f"la altura es {altura} su base {base} y su superficie {superficie}")
    if superficie>12:
        mayor=mayor+1

print(f"la cantidad de triangulos con superficie mayor a 12 son {mayor}")
