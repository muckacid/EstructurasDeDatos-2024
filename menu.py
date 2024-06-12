principal = """+---------------------------------+
|          Menú                   |
+---+-----------------------------+
| 1 | Agregar persona             |
| 2 | Modificar persona           |
| 3 | Eliminar persona            |
| 4 | Ver registro de personas       |
| 5 | Buscar persona por nombre   |
| 6 | Buscar persona por rut      |
| 7 | Buscar persona por apellido |
| 0 | Salir                       |
+---+-----------------------------+"""

salida = """+-----------------------------------+
 |          Menú de salida           |
 +-----------------------------------+
 | Presione 'Intro' para continuar |
 | presione 0 para salir             |                      
 +-----------------------------------+"""

def imprimir_menu(m):
    print(m)
    
def imprimir_mensaje_de_salida():
    texto = "mensaje de salida"
    print(texto)
    
def imprimir_mensaje(mensaje):
    print(mensaje)
    