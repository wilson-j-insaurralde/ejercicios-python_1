"""Elaborar una función que reciba tres enteros y nos retorne el valor promedio de los mismos."""
def promedio(x,y,z):
    prom=(x+y+z)/3
    return prom
def carga():
    num1=int(input("ingrese el primer numero: "))
    num2=int(input("ingrese el segundo numero: "))
    num3=int(input("ingrese el tercer numero: "))
    return num1,num2,num3

n1,n2,n3=carga()
print (f"el promedio de los tres numeros ingresado es: " )
print(promedio(n1,n2,n3))