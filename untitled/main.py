from pessoa import Pessoa
from produto import Produto
from dados import BaseDeDados
from classes.escritor import Escritor
from classes.caneta import Caneta
from classes.heranca import Aluno
from classes.heranca import Cliente
from classes.smartphone import SmartPhone
from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def falar(self):
        pass

class B(A):
    def falar(self):
        print('Falando em B')

b = B()
b.falar()






'''''''''''
p1 = Produto('camiseta', 50)
p1.desconto(10)
print(p1.preco)

p2 = Produto('caneca', 'R$50')
p2.desconto(10)
print(p2.preco)
'''
'''
bd = BaseDeDados()
bd.inserir_cliente(1, 'walter')
bd.inserir_cliente(2, 'Evelin')
bd.inserir_cliente(3, 'Elisa')

bd.apaga_cliente(3)
bd.lista_clientes()


escritor = Escritor('Antonio')
print(escritor.nome)
caneta = Caneta('Preta')
print(caneta.cor)
escritor.ferramenta = caneta
escritor.ferramenta.escrever()


zequinha = Aluno('Zequinha', 12)
zequinha.comer('Pizza')
zequinha.estudar()

smartphone = SmartPhone('J5')
smartphone.ligar()
smartphone.conectar()
smartphone.conectar()

smartphone2 = SmartPhone('iphone')

smartphone2.conectar()
'''