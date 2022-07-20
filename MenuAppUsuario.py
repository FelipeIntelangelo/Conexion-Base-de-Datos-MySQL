from Usuario import Usuario
from UsuarioDao import UsuarioDAO
from logger_base import log

opcion = None

while opcion != 5:
    print('1. Listar usuarios')
    print('2. Agregar usuario')
    print('3. Modificar usuario')
    print('4. Eliminar usuario')
    print('5. Salir')
    opcion = int(input('Elegir una opcion (1-5): '))

    if opcion == 1:
        usuarios = UsuarioDAO.seleccionar()
        for usuario in usuarios:
            log.info(usuario)
    elif opcion == 2:
        Usuario_var = input('Escribe el username: ')
        Password_var = input('Escriba la password: ')
        NewAccount = Usuario(username=Usuario_var, password=Password_var)
        usuarios_insertados = UsuarioDAO.insertar(NewAccount)
        log.info(f'Usuarios insertados: {usuarios_insertados}')
    elif opcion == 3:
        id_a_modificar = int(input('Escribe el id del usuario a modificar: '))
        NuevoUsername = input('Escribe el nuevo nombre de usuario: ')
        NuevaPassword = input('Escriba la nueva contraseña: ')
        usuario_a_actualizar = Usuario(id_a_modificar, NuevoUsername, NuevaPassword)
        usuario_actualizado = UsuarioDAO.actualizar(usuario_a_actualizar)
        log.info(f'usuarios actualizados: {usuario_actualizado}')
    elif opcion == 4:
        id_a_eliminar = int(input('Escriba el id del usuario a eliminar: '))
        usuario_a_eliminar = Usuario(id_usuario=id_a_eliminar)
        usuario_eliminado = UsuarioDAO.eliminar(usuario_a_eliminar)
        log.info(f'Usuarios eliminados: {usuario_eliminado}')
else:
    log.info('Salimos de la aplicacion')
