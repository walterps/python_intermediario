#Testando o encapsulamento em Python
#Com um _ o atributo fica oculto mas é possivel acessar(parecido com o protected)
#Com dois __o atributo fica totalmente proibido de ser acessado

class BaseDeDados:
    def __init__(self):
        self._dados = {}

    @property
    def dados(self):
        return self._dados
    
    def inserir_cliente(self, id, nome):
        if 'clientes' not in self._dados:
            self._dados['clientes'] = {id: nome}
        else:
            self._dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self._dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self._dados['clientes'][id]
