from pessoa import Pessoa

class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nome}  esta comprando')

class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nome} esta estudando ')
