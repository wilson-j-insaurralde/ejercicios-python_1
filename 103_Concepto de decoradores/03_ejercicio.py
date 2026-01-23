"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

import random
import time

# Decorador para medir tiempo
def medir_tiempo(func):
    def envoltura(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"Tiempo {func.__name__}: {fin - inicio:.4f} segundos")
        return resultado
    return envoltura

# Ordenamiento Burbuja
@medir_tiempo
def burbuja(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# Ordenamiento Quicksort (función pública con decorador)
@medir_tiempo
def quicksort(lista):
    def _quicksort(arr):
        if len(arr) <= 1:
            return arr
        pivote = arr[len(arr) // 2]
        izquierda = [x for x in arr if x < pivote]
        medio = [x for x in arr if x == pivote]
        derecha = [x for x in arr if x > pivote]
        return _quicksort(izquierda) + medio + _quicksort(derecha)
    
    return _quicksort(lista)

# Generar listas con 10000 elementos aleatorios
lista1 = [random.randint(0, 100000) for _ in range(10000)]
lista2 = [random.randint(0, 100000) for _ in range(10000)]

# Ejecutar
burbuja(lista1)   
quicksort(lista2)



"""
El decorador medir_tiempo:

def medir_tiempo(func):
    def envoltura(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"Tiempo {func.__name__}: {fin - inicio:.4f} segundos")
        return resultado
    return envoltura
Un decorador recibe como parámetro una función (func).

Define una función interna (envoltura) que envuelve a la original.

Dentro de la función 'envoltura':
Se toma el tiempo antes de ejecutar (inicio = time.time())
Se llama a la función original (resultado = func(*args, **kwargs)).
Se toma el tiempo después (fin = time.time()).
Se imprime cuánto tardó (fin - inicio).
Finalmente, devuelve el resultado original de la función.

Ahora cuando escribimos:

@medir_tiempo
def burbuja(lista):
    .........
Es lo mismo que hacer:

burbuja = medir_tiempo(burbuja)
O sea: cada vez que se llama a burbuja(), en realidad se ejecuta envoltura().

El bloque principal:

# Generar listas con 10000 elementos aleatorios
lista1 = [random.randint(0, 100000) for _ in range(10000)]
lista2 = [random.randint(0, 100000) for _ in range(10000)]

# Ejecutar
burbuja(lista1)   
quicksort(lista2)
burbuja(lista1)
Aquí llamas a la función burbuja y le pasas la lista lista1 (que tiene 10.000 números aleatorios).
Como burbuja está decorada con @medir_tiempo, en realidad no se ejecuta directamente la función burbuja que ordena, sino la función envoltura del decorador.

El flujo real es este:
envoltura toma nota del tiempo inicial (inicio = time.time()).
Llama a la función original burbuja(lista1), que hace el ordenamiento burbuja.
Cuando termina, toma nota del tiempo final (fin = time.time()).
Calcula la diferencia y la imprime en pantalla:

Tiempo burbuja: X.XXXX segundos
Devuelve la lista ya ordenada.
Resultado: lista1 queda ordenada con Burbuja, y además se muestra cuánto tiempo tardó.

Un decorador básico sigue un patrón muy específico
Es una función que toma otra función como su único argumento.
Define una función anidada (o envoltura) dentro de sí misma. Esta función anidada es la que contendrá la lógica adicional que queremos aplicar.
Dentro de la función anidada, se llama a la función original que se pasó como argumento.
La función anidada retorna el resultado de la función original.
Finalmente, el decorador retorna la función anidada (o envoltura).


"""