from classes.eletronico import Eletronico
from classes.log import LogMixin

class SmartPhone(Eletronico, LogMixin):
    def __init__(self, nome):
        super().__init__(nome)
        self._conectado = False

    def conectar(self):
        if not self._ligado:
            info = f'{self._nome} não esta ligado.'
            print(info)
            self.log_info(info)
            return
        if self._conectado:
            error = f'{self._nome} esta conectando ! !'
            self.log_error(error)
        self._conectado = True


    def desconectar(self):
        if not self._conectado:
            print(f'{self._nome} não esta conectado.')
            return
        self._ligado = False

