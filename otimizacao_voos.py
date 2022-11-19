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

## Montar o dicionario de todas as combinacoes possiveis de voos (chaves)
voos = {}
for linha in open('voos.txt'):
    _origem, _destino, _saida, _chegada, _preco = linha.split(',') # '_' para deixar as variaveis como locais (apenas no/dentro do 'for')
    voos.setdefault((_origem, _destino), []) # define o item com as chaves especificadas
    voos[(_origem, _destino)].append((_saida, _chegada, int(_preco))) # para cada origem e destino, define as possiveis combinacoes de saida, chegada e preco 

## Imprimir agenda (cronograma)
# Forma de representar a solucao, no caso, uma lista de numeros.
# [1,4, 3,2, 7,3, 6,3, 2,4, 5,3]
# Seis pessoas, doze posicoes.
# Lista de nrs com seis pessoas e doze posicoes correspondentes as linhas contendo os voos que cada pessoa vai pegar.
# Assim sendo, os voos da Amanda, Pedro, Marcos... respectivamente. 
# Ficando mais claro, a Amanda pegara o primeiro voo (da lista descrita no dicionario) na ida, e o quarto na volta.
def imprimir_agenda(agenda):
    id_voo = -1 # essa variavel e usada para percorrer cada uma das linhas do dicionario (voos) (-1 pq sera incrementada += e a primeira posicao no Python e 0)
    for i in range(len(agenda) // 2): # se eu tenho seis posicoes, 
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
    minutos = x[3] * 60 + x[4] # essas posicoes vem do comando: time.strptime('23:59', '%H:%M')
    return minutos

get_minutos('6:13')
get_minutos('01:00')
get_minutos('23:59')

## Funcao custo
# tempo e custo da viagem
# penalidade de R$ 50 se o carro for devolvido com atraso
# pressuposto que todas as pessoas vao deixar o aeroporto ao mesmo tempo quando a ultima chegar
def funcao_custo(solucao):
    preco_total = 0
    ultima_chegada = 0
    primeira_partida = 1439 # 23:59 --> o voo mais tarde (ver get_minutos com este horario)

    id_voo = -1
    for i in range(len(solucao) // 2):
        origem = pessoas[i][1] # percorre a lista de pessoas, que contem as pessoas e origens
        id_voo += 1
        ida = voos[(origem, destino)][solucao[id_voo]] # horario da ida
        id_voo += 1
        volta = voos[(destino, origem)][solucao[id_voo]] # horario da volta

        preco_total += ida[2]

        if ultima_chegada < get_minutos(ida[1]):
            ultima_chegada = get_minutos(ida[1])
            
        if primeira_partida > get_minutos(volta[0]):
            primeira_partida = get_minutos(volta[0])
            
    total_espera = 0
    id_voo = -1
    for i in range(len(solucao) // 2):
        origem = pessoas[i][1]
        id_voo += 1
        ida = voos[(origem, destino)][solucao[id_voo]]
        id_voo += 1
        volta = voos[(destino, origem)][solucao[id_voo]]
        
        total_espera += ultima_chegada - get_minutos(ida[1])
        total_espera += get_minutos(volta[0]) - primeira_partida
        
    if ultima_chegada > primeira_partida:
        preco_total += 50
        
    return preco_total + total_espera
        
funcao_custo(agenda)  

