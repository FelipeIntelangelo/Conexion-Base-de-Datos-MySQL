import logging as log

log.basicConfig(level=log.INFO,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('UsuarioDB.log'),
                    log.StreamHandler()
                ])
if __name__ == '__main__':
    log.debug('DEBUG')