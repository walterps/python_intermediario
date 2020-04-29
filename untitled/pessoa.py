class Pessoa:

    #Criando o método
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já esta comendo')
            return

        print(f'{self.nome} esta comendo {alimento}.')
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não esta comendo')
            return
        else:
            print(f'{self.nome} parou de comer !')
            self.comendo = False

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} esta comendo ')
        else:
            print(f'{self.nome} esta falando sebre {assunto} ')

