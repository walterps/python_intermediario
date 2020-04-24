#Testando argumentos *args que é uma lista de argumentos variável sem palavras-chaves e em forma de tupla
#Testando argumentos **kwargs que é uma lista de argumentos variavel com palavras-chaves e em forma de tupla

def funcao(*args, **kwargs):
    print(args)

    nome = kwargs.get('nome')

    if nome is not None:
        print(nome)

lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9]

funcao(lista1, lista2, nome=input('informe seu nome:'))
