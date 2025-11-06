"""
En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500, realizar un programa que lea los sueldos que cobra cada empleado e informe cuántos empleados cobran entre $100 y $300 y cuántos cobran más de $300. Además el programa deberá informar el importe que gasta la empresa en sueldos al personal.
"""

n=int(input("ingrese el numero de empleados"))
x=1
cont1=0
cont2=0
importe=0
while x<=n: 
    nombre=str(input("ingrese el nombre del empleado"))
    sueldo=int(input("ingrese el sueldo del empleado"))
    importe=sueldo+importe
    if sueldo>=100 and sueldo<=300 :
        cont1=cont1+1
    else :
        cont2=cont2+1
    x=x+1    
print (f"la cantidad de empleados que cobran entre $100 y $300 son: {cont1}")
print (f"la cantidad de empleados que cobran mas de $300 son: {cont2}")
print (f"el importe total en sueldos es: {importe}")

    
