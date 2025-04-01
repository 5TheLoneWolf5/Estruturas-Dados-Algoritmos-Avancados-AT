"""

Resultado:

Aresta  Peso
0 - 1    2
1 - 2    3
0 - 3    6
1 - 4    5

- Tempo (grafo pequeno): 0.0003325939178466797

Aresta  Peso
0 - 1    4
8 - 2    5
2 - 3    2
5 - 4    3
6 - 5    5
3 - 6    4
8 - 7    3
9 - 8    4
0 - 9    3
9 - 10   2
10 - 11          3
11 - 12          5
12 - 13          4
13 - 14          3

- Tempo (grafo grande): 0.0007748603820800781

Explicação:

Nos casos testados, existe uma diferença leve, onde o grafo pequeno é mais rápido. Mas é algo de todo modo notável. Em todos os casos o grafo pequeno se sai um pouco melhor no critério temporal.

Este algoritmo pode se tornar computacionalmente custoso com uma grande massa de dados envolvida. Implementar uma lista adjacente, dependendo do caso, pode ser uma boa alternativa para melhorar o desempenho.

"""

import sys
import random
import time

class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def printMST(self, parent):
        print("Aresta \tPeso")
        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", self.graph[parent[i]][i])
    def minKey(self, key, mstSet):
        min = sys.maxsize
        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v

        return min_index

    def primMST(self):
        key = [sys.maxsize] * self.V
        parent = [None] * self.V
        key[0] = 0
        mstSet = [False] * self.V

        parent[0] = -1

        for cout in range(self.V):
            u = self.minKey(key, mstSet)
            mstSet[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and mstSet[v] == False \
                and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.printMST(parent)

small_graph = Graph(5)
small_graph.graph = [
    [0,  2,  0,  6,  0],
    [2,  0,  3,  8,  5],
    [0,  3,  0,  0,  7],
    [6,  8,  0,  0,  9],
    [0,  5,  7,  9,  0]
]

start = time.time()

small_graph.primMST()

end = time.time()

print(f"- Tempo (grafo pequeno): {end - start}")

big_graph = Graph(15)

big_graph.graph = [
    [  0,   4,   0,   0,   8,   0,   0,   0,   0,   3,   0,   0,   0,   0,   0],
    [  4,   0,   7,   0,   0,   6,   0,   0,   0,   0,   9,   0,   0,   0,   0],
    [  0,   7,   0,   2,   0,   0,   0,   0,   5,   0,   0,   0,   0,   0,   0],
    [  0,   0,   2,   0,   0,   0,   4,   0,   0,   0,   0,   8,   0,   0,   0],
    [  8,   0,   0,   0,   0,   3,   0,   0,   0,   0,   0,   0,   6,   0,   0],
    [  0,   6,   0,   0,   3,   0,   5,   0,   0,   0,   0,   0,   0,   7,   0],
    [  0,   0,   0,   4,   0,   5,   0,   6,   0,   0,   0,   0,   0,   0,   0],
    [  0,   0,   0,   0,   0,   0,   6,   0,   3,   0,   0,   0,   0,   0,   9],
    [  0,   0,   5,   0,   0,   0,   0,   3,   0,   4,   0,   0,   0,   0,   0],
    [  3,   0,   0,   0,   0,   0,   0,   0,   4,   0,   2,   0,   0,   0,   0],
    [  0,   9,   0,   0,   0,   0,   0,   0,   0,   2,   0,   3,   0,   0,   0],
    [  0,   0,   0,   8,   0,   0,   0,   0,   0,   0,   3,   0,   5,   0,   0],
    [  0,   0,   0,   0,   6,   0,   0,   0,   0,   0,   0,   5,   0,   4,   0],
    [  0,   0,   0,   0,   0,   7,   0,   0,   0,   0,   0,   0,   4,   0,   3],
    [  0,   0,   0,   0,   0,   0,   0,   9,   0,   0,   0,   0,   0,   3,   0],
]

start = time.time()

big_graph.primMST()

end = time.time()

print(f"- Tempo (grafo grande): {end - start}")