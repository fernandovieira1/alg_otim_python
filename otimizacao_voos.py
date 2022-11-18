import time
import random
import math

## Pessoas e locais de origem
pessoas = [('Amanda', 'CWB'),
          ('Pedro', 'GIG'),
          ('Marcos', 'POA'),
          ('Priscila', 'FLN'),
          ('Jessica', 'CNF'),
          ('Paulo', 'GYN')]

# Local de destino
destino = 'GRU'

## Montar o dicionario de todas as combinacões possiveis de voos (chaves)
voos = {}
for linha in open('voos.txt'):
    _origem, _destino, _saida, _chegada, _preco = linha.split(',') # '_' para deixar as variaveis como locais (apenas no/dentro do 'for')
    voos.setdefault((_origem, _destino), []) # define o item com as chaves especificadas
    voos[(_origem, _destino)].append((_saida, _chegada, int(_preco))) # para cada origem e destino, define as possiveis combinacões de saida, chegada e preco 

## Imprimir agenda (cronograma)
# Forma de representar a solucao, no caso, uma lista de números.
# [1,4, 3,2, 7,3, 6,3, 2,4, 5,3]
# Seis pessoas, doze posicões.
# Lista de nrs com seis pessoas e doze posicões correspondentes às linhas contendo os voos que cada pessoa vai pegar.
# Assim sendo, os voos da Amanda, Pedro, Marcos... respectivamente. 
# Ficando mais claro, a Amanda pegara o primeiro voo (da lista descrita no dicionario) na ida, e o quarto na volta.
def imprimir_agenda(agenda):
    id_voo = -1 # essa variavel e usada para percorrer cada uma das linhas do dicionario (voos) (-1 pq sera incrementada += e a primeira posicao no Python e 0)
    for i in range(len(agenda) // 2): # se eu tenho seis posicões, 
        nome = pessoas[i][0] # primeira coluna
        origem = pessoas[i][1] # segunda coluna
        id_voo += 1
        ida = voos[(origem, destino)][agenda[id_voo]]
        id_voo += 1
        volta = voos[(destino, origem)]
        print('%10s%10s %5s-%5s R$%3s %5s-%5s R$%3s' % (nome, origem, ida[0], ida[1], ida[2],
                                                                             volta[0], volta[1], volta[2]))

agenda = [1,4, 3,2, 7,3, 6,3, 2,4, 5,3] # nao entendi direito isso aqui

imprimir_agenda(agenda)

## Conversao em minutos do tempo (em horas)
def get_minutos(hora):
    x = time.strptime(hora, '%H:%M')
    minutos = x[3] * 60 + x[4]
    return minutos

get_minutos('6:13')