"""
Confeccionar una clase que administre una agenda personal. Se debe almacenar el nombre de la persona, teléfono y mail
Debe mostrar un menú con las siguientes opciones:
1- Carga de un contacto en la agenda.
2- Listado completo de la agenda.
3- Consulta ingresando el nombre de la persona.
4- Modificación de su teléfono y mail.
5- Finalizar programa.
"""

class agenda():
    def __init__(self):
      self.contactos={}

    def cargar(self):
        print("--------------------------------------------------")
        seguir="s"
        while seguir=="s":
            nombre=input("ingrese el nombre de la persona: ")
            telefono=int(input("ingrese el numero de telefono: "))
            email=input("ingrese el email: ")
            self.contactos[nombre]=(telefono,email)
            seguir=input("desea seguir a gregando contactos?[s/n]")
        print("--------------------------------------------------")
    
    def listar(self):
        print("--------------------------------------------------")
        print("listado de la agenda: ")
        for nombre in (self.contactos):
            print(nombre,self.contactos[nombre][0],self.contactos[nombre][1] )
        print("--------------------------------------------------")
        
    def consultar(self):
        print("--------------------------------------------------")
        nombre=input("ingrese el nombre a consultar: ")
        if nombre in (self.contactos):
               print(nombre," su telefono es",self.contactos[nombre][0],"y su mail es",self.contactos[nombre][1])
        else:
                print("no se encuentra dicha persona.")
        print("--------------------------------------------------")

    def modificar(self):
        print("--------------------------------------------------")
        tuki=input("ingrese el nombre de la persona que desea mopdificar el telefono y nombre: ")
        if tuki in (self.contactos):
          ntelefono=int(input("ingrese su nuevo telefono: "))
          nemail=input("ingrese su nuevo email. ")
          self.contactos[tuki]=(ntelefono,nemail)
        else:
          print("no se encuentra dicha persona.")
        print("--------------------------------------------------")

    def menu(self):
     
     con=0
     while con!=5:
          
        print ("1)_ cargar contactos")
        print ("2)_ listar contactos")
        print("3)_ buscar contactos")
        print("4)_ modificar email y telefono ")
        print("5)_ si desea finalizar")
        con=int(input("ingrese el numero: "))
        if con == 1:
            self.cargar()
        elif con== 2 :
             self.listar()
        elif con == 3 :
             self.consultar()
        elif con==4:
             self.modificar()


agenda1=agenda()
agenda1.menu()            