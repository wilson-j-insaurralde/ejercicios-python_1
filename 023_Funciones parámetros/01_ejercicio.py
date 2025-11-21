"""
Confeccionar una aplicación que muestre una presentación en pantalla del programa. Solicite la carga de dos valores y nos muestre la suma. Mostrar finalmente un mensaje de despedida del programa.
"""

def mensaje(mensaje):

    print("****************")
    print(mensaje)
    print("****************")

def suma():
    num1=int(input("ingrese el primer numero: "))
    num2= int(input("ingrese el segundo numero: "))
    suma= num1+num2
    print(f"la suma de los dos numeros es: {suma}")

mensaje("el programa muestra la suma de dos valores ingresados por teclado ")
suma()
mensaje("gracias por utilizar el programa ")
