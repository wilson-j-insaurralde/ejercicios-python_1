"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""


"""
Se tiene una lista con un conjunto de tuplas con los nombres y edades de personas:

personas=[('pedro',33),('ana',3),('juan',13),('carla',45)]
Generar una lista con las personas mayores de edad.
"""
personas=[('pedro',33),('ana',3),('juan',13),('carla',45)]
"esto es asi [ RESULTADO | EL BUCLE | LA CONDICIÓN ]"
personas_mayores=[per for per in personas if per[1]>=18] 
print(personas_mayores)