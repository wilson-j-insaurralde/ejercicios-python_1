"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""
"""
Crear una función llamada cuenta_regresiva(n)

"""

def cuenta_regresiva(n):
    if n==0:
        print("despege")
        return
    else:
        print(n)
        cuenta_regresiva(n-1)
       

cuentaregresiva=cuenta_regresiva(5)