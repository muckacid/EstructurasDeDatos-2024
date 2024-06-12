class Persona():
    def __init__(self, nombre, apellido, rut):
        self.nombre = nombre
        self.apellido = apellido
        self.rut = rut
        
    def __str__(self):
        retorno = """
        Nombre: {}
        Apellido: {}
        RUT: {}
        """.format(self.nombre, self.apellido, self.rut)
        return retorno