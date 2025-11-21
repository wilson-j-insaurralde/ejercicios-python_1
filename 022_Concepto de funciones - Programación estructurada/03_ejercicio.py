"""
Desarrollar un programa con dos funciones. La primer solicite el ingreso de un entero y muestre el cuadrado de dicho valor. La segunda que solicite la carga de dos valores y muestre el producto de los mismos. LLamar desde el bloque del programa principal a ambas funciones.
"""

def enteroCuadrado():
    ent=int(input("ingrese el numero entero: "))
    cuadrado=ent*ent
    print(f"el cuadrado del numero entero es: {cuadrado}")

def producto():
    num1=int(input("ingrese el primer numero: "))
    num2=int(input("ingrese el segundo numero"))
    producto=num1*num2
    print(f"el producto de ambos numeros es: {producto}")



enteroCuadrado()
producto()
