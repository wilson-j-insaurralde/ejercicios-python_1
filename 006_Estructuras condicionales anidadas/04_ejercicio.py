"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Confeccionar un programa que permita cargar un número entero positivo de hasta tres cifras y muestre un mensaje indicando si tiene 1, 2, o 3 cifras. Mostrar un mensaje de error si el número de cifras es mayor.
"""
num=int(input("Ingrese un valor de hasta tres dígitos positivo:"))
if num<10:
    print("Tiene un dígito")
else:
    if num<100:
        print("Tiene dos dígitos")
    else:
        if num<1000:
            print("Tiene tres dígitos")
        else:
            print("Error en la entrada de datos.")