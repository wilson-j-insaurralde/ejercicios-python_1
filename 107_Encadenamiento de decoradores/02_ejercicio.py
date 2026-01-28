"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Problema 1
Encadenar un decorador de autenticación y otro de llamada.
"""
def autenticar(func):
    def envoltura(*args,**kwargs):
        print("verificando credenciales...")
        #Aquí podrías validar usuario/contraseña, token, etc.
        return func(*args,**kwargs)
    return envoltura
def registrar(func):
    def envoltura(*args,**kwargs):
        print(f"Llamando a {func.__name__} con args={args}, kwargs={kwargs}")
        resultado = func(*args, **kwargs)
        print(f"{func.__name__} ejecutada con éxito")
        return resultado
    return envoltura

@autenticar
@registrar
def transferir(dinero, cuenta_destino):
    print(f"Transfiriendo {dinero} a {cuenta_destino}")
    return True

# Ejecutar
transferir(100, "Cuenta123")


"""
Flujo de ejecución
Primero se aplica @registrar envuelve la función transferir.

Luego se aplica @autenticar envuelve el resultado anterior.

El orden final al llamar transferir(100, "Cuenta123") es:

Verificando credenciales...
Llamando a transferir con args=(100, 'Cuenta123'), kwargs={}
Transfiriendo 100 a Cuenta123
transferir ejecutada con éxito
"""