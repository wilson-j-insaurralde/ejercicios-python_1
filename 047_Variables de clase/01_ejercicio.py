"""
Definir una clase Cliente que almacene un código de cliente y un nombre.
En la clase Cliente definir una variable de clase de tipo lista que almacene todos los clientes que tienen suspendidas sus cuentas corrientes.
Imprimir por pantalla todos los datos de clientes y el estado que se encuentra su cuenta corriente.
"""
class cliente : 
    suspendidos=[]
    def __init__(self,codigo,cliente):
        self.codigo=codigo
        self.cliente=cliente
    def imprimir(self):
        print("codico del cliente: ",self.codigo)
        print("nombre del cliente: ", self.cliente)
        self.esta_suspendido()
    
    def esta_suspendido(self):
        if self.codigo in cliente.suspendidos:
            print ("el cliente esta suspendido")
        else: 
            print("el cliente no esta sus pendido")
    def suspender(self):
        cliente.suspendidos.append(self.codigo)

cliente1=cliente(1,"pepe")
cliente2=cliente(2,"jaimito")
cliente3=cliente(3,"tomas")
cliente4=cliente(4,"wilson")
 
cliente3.suspender()
cliente4.suspender()

cliente1.imprimir()
cliente2.imprimir()
cliente3.imprimir()
cliente4.imprimir()

print(cliente.suspendidos)