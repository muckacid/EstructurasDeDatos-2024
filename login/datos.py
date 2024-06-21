from Usuario import Usuario

lista_autenticados = [
    Usuario("max", "123", 0),
    Usuario("admin", "admin", 1),
    Usuario("vendedor", "123", 2)
]
def obtener_usuario(credencial):
    for usuario in lista_autenticados:
        if(usuario.nombre == credencial.nombre and usuario.clave == credencial.clave):
            return usuario
