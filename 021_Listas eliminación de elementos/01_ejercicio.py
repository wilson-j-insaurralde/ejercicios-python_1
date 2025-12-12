"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Hemos visto que una lista la podemos iniciar por asignación indicando sus elementos.

lista=[10, 20, 30, 40]
También podemos agregarle elementos al final mediante el método append:

lista.append(120)
Si ahora imprimimos la lista tenemos como resultado:

[10, 20, 30, 40, 120]
Otra característica fundamental de las listas en Python es que podemos eliminar cualquiera de sus componentes llamando al método pop e indicando la posición del elemento a borrar:

lista.pop(0)
Ahora si imprimimos la lista luego de eliminar el primer elemento el resultado es:

[20, 30, 40, 120]
Otra cosa que hay que hacer notar que cuando un elemento de la lista se elimina no queda una posición vacía, sino se desplazan todos los elementos de la derecha una posición.

El método pop retorna el valor almacenado en la lista en la posición indicada, aparte de borrarlo.

lista=[10, 20, 30, 40]
print(lista.pop(0)) # imprime un 10
"""

"""
Crear una lista por asignación con 5 enteros. Eliminar el primero, el tercero y el último de la lista.
"""
lista=[10, 20, 30, 40, 50]

print(lista)

lista.pop(0)
lista.pop(1)
lista.pop(2)

print(lista)

"""
Parecería que con esas tres llamadas al método pop se eliminan los tres primeros elementos pero no es así, si imprimimos cada vez que borramos uno veremos que estamos borrando el primero, tercero y quinto.

lista=[10, 20, 30, 40, 50]
print(lista)
# se imprime [10, 20, 30, 40, 50]
lista.pop(0)
print(lista)
# se imprime [20, 30, 40, 50]
lista.pop(1)
print(lista)
# se imprime [20, 40, 50]
lista.pop(2)
# se imprime [20, 40]
print(lista)
"""