"""
Escribir un programa que lea 10 números enteros y luego muestre cuántos valores ingresados fueron múltiplos de 3 y cuántos de 5. Debemos tener en cuenta que hay números que son múltiplos de 3 y de 5 a la vez.
"""
mult3=0
mult5=0
for x in range (10):
    numero=int(input("ingrese el numero: "))
    if numero%3==0:
        print("es multiplo de 3")
        mult3=mult3+1
    if numero%5==0:
        print("es multiplo de 5")
        mult5=mult5+1
print(f"la cantidad multiplo de 3 es: {mult3}")
print(f"la cantidad multiplo de 5 es: {mult5}")