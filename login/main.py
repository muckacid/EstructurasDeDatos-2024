from os import system
from Usuario import *
from validacion import *
from datos import *

while True:
    system("cls")
    nombre = input("->Ingrese su nombre de usuario: ")
    clave = input("->Ingrese su contraseña: ")
    usuario = Usuario(nombre, clave)
    if(validar_usuario(usuario)):
        usuario_val = obtener_usuario(usuario)
        print("Bienvenido ", usuario.nombre)
        # aca llamar al modulo integrado del sistema
    else:
        print("Crendenciales no validas")
    system("pause")
    
