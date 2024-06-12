# Imports
from funciones import *
from menu import *

lista_de_personas = []
while True:
    imprimir_menu(principal)
    opcion_principal = input("Ingresar opcion: ")
    # Opcion (1): Agregar un objeto a la lista
    if opcion_principal == '1':
        imprimir_mensaje("Se ha ingrsado a la popcion de nuevo resgistro de persona")
        while True:
            # Formulacion de registro
            imprimir_mensaje("Nuevo registro")
            # Ingres de dato: nombre, tipo: texto(str)
            nombre = input("Ingrese el nombre: ")
            # Ingres de dato: apellido, tipo: texto(str)
            apellido = input("Ingrese el apellido: ")
            # Ingres de dato: rut, tipo: texto(str)
            rut = input("Ingrese el rut: ")
            
            # --
            agregar_al_registro(crear_persona(nombre, apellido, rut), lista_de_personas)
            imprimir_mensaje("Se ha agregado un objeto a la lista de personas.")

            imprimir_menu(salida)
            opcion_salida = input("Ingrese la opción")
            if opcion_salida == '0':
                imprimir_mensaje("saliendo de agregar registro")
                break
    
    # Modificar un objeto de la lista
    # Eliminar objeto de la lista
    # Ver todos los objetos de la lista
    # Buscar ???????????????????????
    # Salir
    if opcion_principal == '0':
        imprimir_mensaje_de_salida()
        break



