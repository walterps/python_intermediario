#Criando funções no python

'''''''''
def saudacao(msg='Ola', nome='usuario'):
    nome = nome.replace('a', '3')
    msg  = msg.replace('a', '@')
    return f'{nome} {msg}'

variavel = saudacao('Ola, tudo bem ?', 'Walter')
if variavel:
    print(variavel)
else:
    print('Não retornou nenhum valor')


def divisao(n1, n2):
    if n2 > 0:
        resultado = n1/n2
        return resultado

result = divisao(1, 1)
msg = f'O resultado da divisão é {result}' if result else 'Erro na divisão'
print(msg)
'''

def soma(n1, n2, n3):
    resultado = n1+n2+n3
    return resultado

def percentual(n1, perc):
    resultado = n1+(n1*(perc / 100))
    return resultado

ajuste = percentual(100, 10)
print(ajuste)





