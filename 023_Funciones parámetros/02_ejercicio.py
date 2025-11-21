"""
Confeccionar una función que reciba tres enteros y nos muestre el mayor de ellos. La carga de los valores hacerlo por teclado.
"""

def mostrarMayor(num1,num2,num3):
    if num1>num2 and num1>num3:
        print(f"el numero mayor es: {num1}")
    else: 
        if num2>num3:
            print(f"el numero mayor es: {num2}")
        else:
            print(f"el numero mayor es: {num3}")
def cargar():
    num1=int(input("ingrese el primer numero: "))
    num2= int(input("ingrese el segundo numero: "))
    num3=int(input("ingrese el tercer numero: "))
    mostrarMayor(num1,num2,num3)

cargar()
