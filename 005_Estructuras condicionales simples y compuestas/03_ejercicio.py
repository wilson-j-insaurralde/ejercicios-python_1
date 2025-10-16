"""
Realizar un programa que solicite la carga por teclado de dos números, si el primero es mayor al segundo informar su suma y diferencia, en caso contrario informar el producto y la división del primero respecto al segundo.
"""

num1=int(input("ingrese el primer numero: "))
num2=int(input("ingrese el segundo numero: "))

if (num1>num2):
    suma=num1+num2
    resta=num1-num2
    print("la suma de los numeros es: ",suma)
    print("la diferencia entre los numeros es: ",resta)
else :
    producto=num1*num2
    division=num2/num1
    print("el producto es: ",producto)
    print("la division es: ",division)