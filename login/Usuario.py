class Usuario:
    def __init__(self, nombre, clave, nivel=0):
        self.nombre = nombre
        self.clave = clave
        self.nivel = nivel
        # nivel 0 usuario generico
        # nivel 1 usuario administrador
        # nivel 2 usuario empleado
        
    def __str__(self) -> str:
        return f"Nombre: {self.nombre}\nClave: {self.clave}"