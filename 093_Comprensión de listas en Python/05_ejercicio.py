"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Codificar un programa que muestre en pantalla los números del 1 al 100, sustituyendo los múltiplos de 3 por el palabra "Fizz" y, a su vez, los múltiplos de 5 por "Buzz". Para los números que, al tiempo, son múltiplos de 3 y 5, mostrar el mensaje "FizzBuzz".
"""

for x in range(1,101):
    if x%3==0 and x%5==0:
        print("FizzBuzz")
    elif x%3==0:
        print("Fizz")
    elif x%5==0:
        print("Buzz")
    else:
        print(x)

    #resuelto de la otra forma 
    print("_____________________________________________")
    x=0
    print(["Fizz"*(not x%3)+"Buzz"*(not x%5) or x for x in range (1,101)])