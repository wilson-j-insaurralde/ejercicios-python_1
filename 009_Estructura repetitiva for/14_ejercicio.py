"""
Escribir un programa que pida ingresar coordenadas (x,y) que representan puntos en el plano.
Informar cuántos puntos se han ingresado en el primer, segundo, tercer y cuarto cuadrante. Al comenzar el programa se pide que se ingrese la cantidad de puntos a procesar.
"""

n=int(input("ingrese la cantidad de puntos a procesar: "))

for x in range (n):
    x=int(input("ingrese la cordenada x: "))
    y=int (input("ingrese la cordenada y: "))
    if x>0 and y>0: 
        primer=primer+1
    else: 
        if x<0 and y>0:
            segundo=segundo+1       
        else:
            if x<0 and y<0:
                tercero=tercero+1
            else: 
                cuarto=cuarto+1

print(f"puntos en el primer cuadrante: {primer}")
print(f"puntos en el segundo cuadrante: {segundo}")
print(f"puntos en el tecer cuadrante: {tercero}")
print(f"puntos en el cuarto cuadrante: {cuarto}")