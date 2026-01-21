"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""


"""
Si el recurso no se encuentra en el servidor de internet o se genera cualquier otro tipo de error, podemos capturar la excepción 'HTTPError' del paquete 'urllib'

Confeccionaremos un script que intente recuperar una página HTML que no se encuentre en el servidor:

http://www.scratchya.com.ar/pythonya/ejercicio336/paginax.html
luego capturaremos la excepción 'HTTPError'
"""
from urllib import request
from urllib import error

try:
    pagina=request.urlopen("http://www.scratchya.com.ar/pythonya/ejercicio336/paginax.html")
    datos=pagina.read().decode("utf-8")
    print(datos)
except error.HTTPError as err:
    print(f"Código de respuesta HTTP devuelto por el servidor {err.code}")
    print(f"No existe el recurso {err.filename}")