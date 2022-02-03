import time
import random
import math

pessoas = [('Amanda', 'CWB'),
          ('Marcos', 'GIG'),
          ('Priscila', 'FLN'),
          ('Jessica', 'OFN'),
          ('Paulo', 'GYN')]

destino = 'GRL'

voos = {}
for linha in open('voos.txt'):
    #print(linha)
    _origem, _destino, _saida, _chegada, _preco = linha.split(',') # '_' para deixar as variáveis como locais (apenas no 'for')
    voos.setdefault((_origem, _destino), [])
    voos[(_origem, _destino)].append((_saida, _chegada, int(_preco)))

print(voos['GRU', 'CWB'])