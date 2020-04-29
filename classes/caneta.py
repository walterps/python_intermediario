class Caneta:
    def __init__(self, cor='Azul'):
        self.__cor = cor

    @property
    def cor(self):
        return self.__cor

    def escrever(self):
        print('caneta está escrevendo...')


