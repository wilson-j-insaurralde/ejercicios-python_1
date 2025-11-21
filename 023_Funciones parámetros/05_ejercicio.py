"""
Confeccionar una función que reciba tres enteros y los muestre ordenados de menor a mayor. En otra función solicitar la carga de 3 enteros por teclado y proceder a llamar a la primer función definida.
"""
def ordenar(num1,num2,num3):
    if num1>num2 and num1>num3:
        if num2>num3:
            print(num3,num2,num1)
        else: 
            print(num2,num3,num1)
    else: 
            if num2>num3:
                 if num1>num3:
                      print (num3,num1,num2)
                 else: 
                      print(num1,num3,num2)
            else: 
                 print(num1,num2,num3)

def cargaDenumeros():
     x=int(input("ingrese el primer numero: "))
     y=int(input("ingrese el segundo numero: "))
     z=int(input("ingrese el tercer numero: "))
     ordenar(x,y,z)

cargaDenumeros()               