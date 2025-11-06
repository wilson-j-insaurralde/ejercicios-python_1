"""
Codificar un programa que solicite la carga de un valor positivo y nos muestre desde 1 hasta el valor ingresado de uno en uno.
Ejemplo: Si ingresamos 30 se debe mostrar en pantalla los números del 1 al 30.

Es de FUNDAMENTAL importancia analizar los diagramas de flujo y la posterior codificación en Python de los siguientes problemas, en varios problemas se presentan otras situaciones no vistas en el ejercicio anterior.
"""

"""
Podemos observar que se ingresa por teclado la variable n. El operador puede cargar cualquier valor.
Si el usuario carga 10 el bloque repetitivo se ejecutará 10 veces, ya que la condición es “Mientras x<=n ”, es decir “mientras x sea menor o igual a 10”; pues x comienza en uno y se incrementa en uno cada vez que se ejecuta el bloque repetitivo.
"""
n=int(input("Ingrese el valor final:"))
x=1
while x<=n:
    print(x)
    x=x+1   
"""
Los nombres de las variables n y x pueden ser palabras o letras (como en este caso)

La variable x recibe el nombre de CONTADOR. Un contador es un tipo especial de variable que se incrementa o disminuye con valores constantes durante la ejecución del programa.
El contador x nos indica en cada momento la cantidad de valores impresos en pantalla.
"""