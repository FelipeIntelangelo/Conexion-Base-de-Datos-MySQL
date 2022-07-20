from logger_base import log
from Conexion import Conexion

class CursorDelPool:
    def __init__(self):
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        log.debug('Inicio del metodo with __enter__')
        self._conexion = Conexion.ObtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor

    def __exit__(self, tipo_excepcion, valor_excepcion, detalle_excepcion):
        log.debug('Inicio del metodo with __exit__')
        if valor_excepcion:
            self._conexion.rollback()
            log.error(f'Ocurrio una excepcion, rollback en camino: {valor_excepcion}, {tipo_excepcion}, {detalle_excepcion}')
        else:
            self._conexion.commit()
            log.debug('Commit de la transaccion')
        self._cursor.close()
        Conexion.liberarConexion(self._conexion)