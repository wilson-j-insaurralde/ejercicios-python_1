"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""
"""Recorrer un árbol de directorios en forma recursiva. Mostrar de cada directorios los archivos y directorios, luego descender a cada directorio y hacer la misma actividad."""
import os 

def leer(directorio):
    # 1. Obtenemos la lista de nombres
    lista = os.listdir(directorio)
    
    for elemento in lista:
        # IMPORTANTE: Unimos la carpeta con el nombre del archivo
        ruta_completa = os.path.join(directorio, elemento)
        
        if os.path.isfile(ruta_completa):
            print(elemento + " [archivo]")
            
        elif os.path.isdir(ruta_completa):
            print("\n--- Entrando a carpeta: " + elemento + " ---")
            # LLAMADA RECURSIVA: Entra a la subcarpeta
            leer(ruta_completa) 
            print("--- Saliendo de carpeta: " + elemento + " ---\n")

# Probá con tu ruta (asegurate que termine en / o usar os.path.join)
leer("C:/Users/wiliam/Desktop/repos/ejercicios-python_1")




"""
import os

def leer(directorio):
    lista = os.listdir(directorio)
    for elemento in lista:
        if os.path.isfile(directorio+elemento):
            print(elemento+" [archivo]")
        if os.path.isdir(directorio+elemento):
            print(elemento+" [directorio]")
            leer(directorio+elemento+"/")

leer("C:/Users/wiliam/Desktop/repos/ejercicios-python_1/") 



"""