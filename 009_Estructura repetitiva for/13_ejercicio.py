"""
Realizar un programa que lea los lados de n triángulos, e informar:
a) De cada uno de ellos, qué tipo de triángulo es: equilátero (tres lados iguales), isósceles (dos lados iguales), o escaleno (ningún lado igual)
b) Cantidad de triángulos de cada tipo.
"""
n=int(input("ingrese la cantidad de triangulos: "))
equilatero=0
isoceles=0
escaleno=0

for x in range(n):
    lado1=int(input("ingrese el primer lado: "))
    lado2=int(input("ingrese el segundo lado: "))
    lado3=int(input("ingrese el tercer lado: "))

    if lado1 == lado2 == lado3 :
        equilatero=equilatero+1
        print("es equilatero.")
    else:
        if lado1==lado2 or lado1==lado3 or lado2==lado3:
            isoceles= isoceles+1
            print("es isoceles.")
        else :
            escaleno=escaleno+1
            print("es escaleno.")

print(f"la cantidad de equilateros es: {equilatero}")  
print(f"la cantidad de isoceles es: {isoceles}")
print(f"la cantidad de escaleno: {escaleno}")      

