"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Creación una función que reciba como parámetro el nombre del jugador, luego tira dos dados y muestra el mensaje que gano si suma 7 y perdió en caso contrario. Crear una función decoradora que grabe en un archivo que se le pasa a la función decoradora el resultado de la tirada de los dos dados.
"""

def decarodor_parametrizado(mensaje):
    def decorador(func):
        def envoltura (*args,**kwargs):
            print(f"{mensaje}- Antes de la funcion")
            resultado=func (*args,**kwargs)
            print(f"{mensaje}- despues de la funcion")
            return resultado
        return envoltura
    return decorador
@decarodor_parametrizado("depuracion")
def principal():
    print("funcion principal ejecutandose.")
principal()


            
