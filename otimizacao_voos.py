import time
import random
import math

pessoas = [('Amanda', 'CWB'),
          ('Pedro', 'GIG'),
          ('Marcos', 'POA'),
          ('Priscila', 'FLN'),
          ('Jessica', 'CNF'),
          ('Paulo', 'GYN')]

destino = 'GRU'

voos = {}
for linha in open('voos.txt'):
    #print(linha)
    _origem, _destino, _saida, _chegada, _preco = linha.split(',') # '_' para deixar as variáveis como locais (apenas no 'for')
    voos.setdefault((_origem, _destino), [])
    voos[(_origem, _destino)].append((_saida, _chegada, int(_preco)))

# [1,4, 3,2, 7,3, 6,3, 2,4, 5,3]
# Lista de nrs com seis pessoas e doze posições correspondentes às linhas contendo os vôos que cada pessoa vai pegar
def imprimir_agenda(agenda):
    id_voo = -1
    for i in range(len(agenda) // 2):
        nome = pessoas[i][0]
        origem = pessoas[i][1]
        id_voo += 1
        ida = voos[(origem, destino)][agenda[id_voo]]
        id_voo += 1
        volta = voos[(destino, origem)]
        print('%10s%10s %5s-%5s R$%3s %5s-%5s R$%3s' % (nome, origem, ida[0], ida[1], ida[2],
                                                                             volta[0], volta[1], volta[2]))

agenda = [1,4, 3,2, 7,3, 6,3, 2,4, 5,3]

imprimir_agenda(agenda)