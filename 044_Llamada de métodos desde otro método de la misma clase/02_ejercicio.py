"""
Plantear una clase que administre dos listas de 5 nombres de alumnos y sus notas. Mostrar un menú de opciones que permita:
1- Cargar alumnos.
2- Listar alumnos.
3- Mostrar alumnos con notas mayores o iguales a 7.
4- Finalizar programa.
"""
class alumnos():

    def __init__ (self):
        self.alumnoslis=[]
        self.notaslist=[]

    def cargar(self):
        seguir="s"
        while seguir=="s":
            alumno=input("ingrese el nombre del alumno: ")
            nota=int(input("ingrese la nota del alumno: "))
            self.alumnoslis.append(alumno)
            self.notaslist.append(nota)
            seguir=input("desea seguir cargando alumnos: [s/n]")

    def listaralumnos(self):
        print("_____________________") 
        print("lista de los alumnos: ")
        for x in range (len(self.alumnoslis)):
            print(self.alumnoslis[x],self.notaslist[x],sep=" --- ")
        print("_____________________") 
    def notasmayoresiguala7(self):
        print("_____________________") 
        print("alumnos lista con notas igual o mayor a 7: ")
        for x in range(len(self.alumnoslis)):
           
            if (self.notaslist[x])>=7:
                print(self.alumnoslis[x],self.notaslist[x],sep=" --- ") 

        print("_____________________") 
    def menu(self):
        este=0
        while este!=4:
            print("1)--- si desea cargar los alumnos.")
            print("2)--- si desea ver la lista de alumnos")
            print("3)--- si desea ver los alumnos con notas mayores o iguales a 7 ")
            print("4)--- si desea finalizar programa")
            este=int(input("ingrese su opcion: "))
            if este==1:
                self.cargar()
            elif este==2:
                self.listaralumnos()
            elif este==3:
                self.notasmayoresiguala7()


alumnos=alumnos()
alumnos.menu()
            
        
