#REalizar a soma dos valores no carrinho de compras

carrinho = []
carrinho.append(('produto 1', 10))
carrinho.append(('produto 2', 20))
carrinho.append(('produto 3', '15'))

total = sum([float(y) for x, y in carrinho])
print(total)