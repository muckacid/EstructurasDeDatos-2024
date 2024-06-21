from datos import lista_autenticados

def validar_usuario(usuario):
    for crendencial in lista_autenticados:
        if(usuario.nombre == crendencial.nombre and usuario.clave == crendencial.clave):
            return True
    return False

def obtener_usuario(credencial):
    for usuario in lista_autenticados:
        if(usuario.nombre == credencial.nombre and usuario.clave == credencial.clave):
            return usuario
