class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False


    def ligar(self):
        if self._ligado:
            return
        self._ligado = True
        print(f'{self._nome} esta ligando ! !')

    def desligar(self):
        if self._ligado:
            self._ligado = False
        return


