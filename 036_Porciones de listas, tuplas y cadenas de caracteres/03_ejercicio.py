"""
Confeccionar una función que reciba una cadena de caracteres y nos devuelva los tres primeros.
En el bloque principal del programa definir una tupla con los nombres de meses. Mostrar por pantalla los primeros tres caracteres de cada mes.
"""
def losprimerostres(cadena):
    return cadena[:3]


meses=('enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre')

for mes in meses:
    print(losprimerostres(mes))


