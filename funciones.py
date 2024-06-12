from Persona import *

def crear_persona(nombre, apellido, rut):
    persona = Persona(nombre, apellido, rut)
    return persona

def agregar_al_registro(objeto, lista):
    lista.append(objeto)
    
def imprimir_lista(lista):
    for objeto in lista:
        print(objeto)
        
        