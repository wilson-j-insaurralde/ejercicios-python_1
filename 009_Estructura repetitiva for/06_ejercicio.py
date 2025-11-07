"""Escribir un programa que solicite por teclado 10 notas de alumnos y nos informe cuántos tienen notas mayores o iguales a 7 y cuántos menores."""
mayores=0
menores=0
for x in range(10):
    nota=int(input("ingrese la nota del alumno: "))
    if nota>=7:
        mayores=mayores+1
    else: 
        menores=menores+1


print(f"las notas mayores iguales a 7 son: {mayores}")
print(f"las notas menores a 7 son: {menores}")       
