#Testando os gerenciadores de contexto do python


class Arquivo:
    def __init__(self, arquivo, modo):
        print('abrindo arquivo')
        self.arquivo = open(arquivo, modo)

    def __enter__(self):
        print('retornando arquivo')
        return self.arquivo

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('fechando arquivo')
        self.arquivo.close()



with Arquivo('abc.txt', 'w') as arquivo:
    arquivo.write('Olá, texto!')


