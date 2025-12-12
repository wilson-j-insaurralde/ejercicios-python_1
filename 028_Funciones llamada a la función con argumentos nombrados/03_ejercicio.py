"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Elaborar una función que muestre la tabla de multiplicar del valor que le enviemos como parámetro. Definir un segundo parámetro llamado termino que por defecto almacene el valor 10. Se deben mostrar tantos términos de la tabla de multiplicar como lo indica el segundo parámetro.
Llamar a la función desde el bloque principal de nuestro programa con argumentos nombrados.
"""
def multiplicar(numero,multiplicador=10):
    for x in range (1,multiplicador+1):
        va=numero*x
        if x == (multiplicador):
            print(va)
        else:
           print(va,",",sep="",end="")

    

print("Tabla del 3")

multiplicar(3)
print("Tabla del 3 con 5 terminos")
multiplicar(3,5)
print("Tabla del 3 con 20 terminos")
multiplicar(multiplicador=20,numero=3)
