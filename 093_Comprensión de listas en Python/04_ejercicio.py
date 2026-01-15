"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Se tiene una lista de nombres de personas. Generar otra lista cuyos elementos sean a su vez listas con dos nombres cada uno.
Tener en cuenta que nunca se debe combinar el mismo nombre dos veces.
"""
nombres=['juan','pablo','luis','mauro','hector']

nombres_compuestos=[[nombre1,nombre2] for nombre1 in nombres for nombre2 in nombres if nombre1!=nombre2]
print(nombres_compuestos)
