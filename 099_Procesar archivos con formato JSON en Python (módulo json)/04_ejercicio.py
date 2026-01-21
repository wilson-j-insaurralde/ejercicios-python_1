"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""


"""
El sitio web

https://jsonplaceholder.typicode.com/
se puede utilizar para recuperar datos con diferentes formatos (JSON por ejemplo) y probar nuestros algoritmos.

Confeccionar una aplicación en Python que recupere el archivo JSON de la siguiente dirección web:

https://jsonplaceholder.typicode.com/posts
Nos retorna un archivo JSON con un formato similar a:

[
  {
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit
             molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
  },
  {
    "userId": 1,
    "id": 2,
    "title": "qui est esse",
    "body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores 
             neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui 
             aperiam non debitis possimus qui neque nisi nulla"
  }]
Convertir los datos recuperados a una lista y mediante un for mostrar los atributos "userID", "id", "title" y "body".

Ver video
"""

from urllib import request
import json

pagina=request.urlopen("https://jsonplaceholder.typicode.com/posts")
datos=pagina.read().decode("utf-8")
lista=json.loads(datos)
for elemento in lista:
    print("userId:",elemento['userId'])
    print("Id:",elemento['id'])
    print("title:",elemento['title'])
    print("body:",elemento['body'])
    print("_"*80)
