"""
Desarrollar un programa que solicite la carga de 10 números e imprima la suma de los últimos 5 valores ingresados.
"""
cont=0
for x in range(10):
    numero=int(input("ingrese el numero: "))
    if x>4:
        cont=cont+numero

print(f"la suma de los ultimos 5 es: {cont} ")        