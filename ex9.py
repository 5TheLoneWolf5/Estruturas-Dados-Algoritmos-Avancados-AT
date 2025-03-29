"""

Respostas:

Começando pelo vértice A, a ordem é:

A B C D E F

Diferente da DFS que segue um padrão de pilha, a estrutura de dados usada para armazenar os nós temporários é uma fila.

"""

class Grafo:
    def __init__(self):
        self.lista_adjacencia = {}

    def adicionar_vertice(self, vertice):
        if vertice not in self.lista_adjacencia:
            self.lista_adjacencia[vertice] = []

    def adicionar_aresta(self, vertice1, vertice2):
        if vertice1 in self.lista_adjacencia and vertice2 in self.lista_adjacencia:
            self.lista_adjacencia[vertice1].append(vertice2)
            self.lista_adjacencia[vertice2].append(vertice1)

    def bfs(self, inicio):
        visitados = set()
        fila = [inicio]

        while fila:
            vertice = fila.pop(0)
            if vertice not in visitados:
                print(vertice, end=" ")
                visitados.add(vertice)
                fila.extend(self.lista_adjacencia[vertice])

grafo = Grafo()
vertices = ["A", "B", "C", "D", "E", "F"]

for i in vertices:
    grafo.adicionar_vertice(i)

arestas = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "E"), ("D", "F"), ("E", "F")]

for i, j in arestas:
    grafo.adicionar_aresta(i, j)

grafo.bfs("A")
