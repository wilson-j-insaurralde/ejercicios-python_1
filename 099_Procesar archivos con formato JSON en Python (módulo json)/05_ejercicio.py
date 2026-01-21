"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""
"""
Hacer la misma actividad que el problema anterior con el recurso que devuelve la dirección:

https://jsonplaceholder.typicode.com/users
Nos retorna un archivo JSON con un formato similar a:

[
  {
    "id": 1,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "Sincere@april.biz",
    "address": {
      "street": "Kulas Light",
      "suite": "Apt. 556",
      "city": "Gwenborough",
      "zipcode": "92998-3874",
      "geo": {
        "lat": "-37.3159",
        "lng": "81.1496"
      }
    },
    "phone": "1-770-736-8031 x56442",
    "website": "hildegard.org",
    "company": {
      "name": "Romaguera-Crona",
      "catchPhrase": "Multi-layered client-server neural-net",
      "bs": "harness real-time e-markets"
    }
  },
  {
    "id": 2,
    "name": "Ervin Howell",
    "username": "Antonette",
    "email": "Shanna@melissa.tv",
    "address": {
      "street": "Victor Plains",
      "suite": "Suite 879",
      "city": "Wisokyburgh",
      "zipcode": "90566-7771",
      "geo": {
        "lat": "-43.9509",
        "lng": "-34.4618"
      }
    },
    "phone": "010-692-6593 x09125",
    "website": "anastasia.net",
    "company": {
      "name": "Deckow-Crist",
      "catchPhrase": "Proactive didactic contingency",
      "bs": "synergize scalable supply-chains"
    }
  }
]
Convertir los datos recuperados a una lista y mediante un for mostrar todos los atributos.
"""



from urllib import request
import json

pagina=request.urlopen("https://jsonplaceholder.typicode.com/users")
datos=pagina.read().decode("utf-8")
lista=json.loads(datos)
print(lista)
for elemento in lista:   
    print("id:",elemento['id'])
    print("name:",elemento['name'])
    print("username:",elemento['username'])
    print("email:",elemento['email'])
    print("street:",elemento["address"]["street"])
    print("suite:",elemento["address"]["suite"])    
    print("city:",elemento["address"]["city"])
    print("zipcode:",elemento["address"]["zipcode"])
    print("lat:",elemento["address"]["geo"]["lat"])
    print("lng:",elemento["address"]["geo"]["lng"])
    print("phone:",elemento['phone'])
    print("website:",elemento['website'])
    print("company name:",elemento["company"]["name"])
    print("catchPhrase:",elemento["company"]["catchPhrase"])
    print("bs:",elemento["company"]["bs"])
    print("_"*80)