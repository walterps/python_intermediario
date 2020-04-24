#Testando as funções anonimas Lambda- ordenano uma lista

lista = [
    ['p1', 2],
    ['p2', 6],
    ['p3', 4],
]

lista.sort(key=lambda item: item[0])
print(lista)