#Treinando com o dicionario em Python. Sistema de perguntas e respostas.
perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2 ?',
        'respostas': {'a': '1', 'b': '4', 'c': '5'},
    'resposta_certa': 'b',
    },
    'Pergunta 2 ': {
        'pergunta': 'Quanto é 6-1 ?',
        'respostas': {'a': '1', 'b': '2', 'c': '5'},
    'resposta_certa': 'c',
    },
}

print()

respostas_certas = 0
qtd_perguntas = len(perguntas)

for chave_pergunta, valor_pergunta in perguntas.items():
    print(f'{chave_pergunta}: {valor_pergunta["pergunta"]}')
    print('Opções:')

    for chave_resposta, valor_resposta in valor_pergunta['respostas'].items():
        print(f'[{chave_resposta}]: {valor_resposta}')
    resposta = input('Sua resposta:')
    print()
    if resposta == valor_pergunta['resposta_certa']:
        respostas_certas = respostas_certas + 1


print(f'Você acertou {respostas_certas} das {qtd_perguntas} questões')
