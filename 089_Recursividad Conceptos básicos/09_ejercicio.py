"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""


"""
Enunciado: Supongamos que en tu computadora no funciona la tecla de multiplicar (*). Tenés que crear una función recursiva que calcule la multiplicación de dos números a y b usando solo sumas.Ejemplo: $3 \times 4$ es lo mismo que sumar $3 + 3 + 3 + 3$.Pista: Sumás a y llamás a la función restándole 1 a b. Cuando b sea 1, devolvés a.
"""
def multiplicar(a,b):
    if b==0:    
        return 0
    else:
        return a+multiplicar(a,b-1)
multiplicarr=multiplicar(8,4)
print(multiplicarr)