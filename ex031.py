#Geradores, iteradores e iteraveis
'''''''''
lista = [1, 2, 3]
lista = 123

print(hasattr(lista, '__iter__'))


def gera():
    variavel = 'valor 1'
    yield variavel
    variavel = 'valor 2'
    yield variavel
    variavel = 'valor 3'
    yield variavel

g = gera()
print(type(g))

for v in  g:
    print(v)

cidades = ['São Paulo', 'Salvador', 'Bahia']

estados = ['SP', 'MG', 'BA']

cidades_estados = zip(cidades, estados)
cidades_estados = list(cidades_estados)
print(cidades_estados)
'''


from itertools import count

contador = count(start=0, step=1)


for x in contador:
    if x <= 10:
        print(x)
    else:
        print('Ja chegou em 10')
        break




