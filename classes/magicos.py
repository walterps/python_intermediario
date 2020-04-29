#Testando os métodos magicos
#OBS: Em Python todas as classes derivam da classe object

class A:

    def __init__(self):
        print('Olá ')

    '''
    def __call__(self, *args, **kwargs):
        resultado = 1

        for i in args:
            resultado *= i

        return resultado
    '''

    def __setattr__(self, key, value):
        self.__dict__[key] = value
        print(key, value)

    def __del__(self):
        print('Objeto coletado.')

a = A()
a.nome = 'walter'
print(a.nome)
