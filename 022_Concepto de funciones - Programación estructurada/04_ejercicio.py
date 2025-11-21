"""
Desarrollar un programa que solicite la carga de tres valores y muestre el menor. Desde el bloque principal del programa llamar 2 veces a dicha función (sin utilizar una estructura repetitiva)
"""

def carga():
    num1=int(input("ingrese el primer numero: "))
    num2=int(input("ingrese el segundo numero: "))
    num3=int(input("ingrece el tercer numero: "))
    if num1<num2 and num1<num3:
        print(f"el numero {num1} es el maschico de los tres.")
    else: 
        if num2<num3:
            print(f"el numero {num2} es el ,maschico de los tres")
        else: 
            print(f"el numero {num3} es el mas chico de los tres")


carga()
carga()