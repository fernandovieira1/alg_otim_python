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

## Montar o dicionário de todas as combinações possíveis de voos (chaves)
voos = {}
for linha in open('voos.txt'):
    _origem, _destino, _saida, _chegada, _preco = linha.split(',') # '_' para deixar as variáveis como locais (apenas no/dentro do 'for')
    voos.setdefault((_origem, _destino), []) # define o item com as chaves especificadas
    voos[(_origem, _destino)].append((_saida, _chegada, int(_preco))) # para cada origem e destino, define as possíveis combinações de saída, chegada e preço 

## Imprimir agenda (cronograma)
# Forma de representar a solução, no caso, uma lista de números.
# [1,4, 3,2, 7,3, 6,3, 2,4, 5,3]
# Seis pessoas, doze posições.
# Lista de nrs com seis pessoas e doze posições correspondentes às linhas contendo os vôos que cada pessoa vai pegar.
# Assim sendo, os vôos da Amanda, Pedro, Marcos... respectivamente. 
# Ficando mais claro, a Amanda pegará o primeiro vôo (da lista descrita no dicionário) na ida, e o quarto na volta.
def imprimir_agenda(agenda):
    id_voo = -1 # essa variável é usada para percorrer cada uma das linhas do dicionário (voos) (-1 pq será incrementada += e a primeira posição no Python é 0)
    for i in range(len(agenda) // 2): # se eu tenho seis posições, 
        nome = pessoas[i][0] # primeira coluna
        origem = pessoas[i][1] # segunda coluna
        id_voo += 1
        ida = voos[(origem, destino)][agenda[id_voo]]
        id_voo += 1
        volta = voos[(destino, origem)]
        print('%10s%10s %5s-%5s R$%3s %5s-%5s R$%3s' % (nome, origem, ida[0], ida[1], ida[2],
                                                                             volta[0], volta[1], volta[2]))

agenda = [1,4, 3,2, 7,3, 6,3, 2,4, 5,3]

imprimir_agenda(agenda)