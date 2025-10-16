"""Se ingresan tres notas de un alumno, si el promedio es mayor o igual a siete mostrar un mensaje "Promocionado"."""

nota1=int(input("Ingrese primer nota:"))
nota2=int(input("Ingrese segunda nota:"))
nota3=int(input("INgrese la tercer nota:"))
promedio=(nota1 + nota2 + nota3)/3
if promedio>=7:
    print("Promocionado")