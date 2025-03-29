"""

Resposta:

A DFS pode ser mais eficiente que a BFS em encontrar caminhos de labirintos, detecção de ciclos, no solucionamento de quebra-cabeças como Sudoku e outros.

Enquanto isso, a BFS pode ser mais eficiente que a DFS em encontrar o caminho mais curto em um grafo não ponderado, análise de amigos em uma rede social, web crawling e outros.

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

    def mostrar_grafo(self):
        for vertice in self.lista_adjacencia:
            print(f"{vertice} -> {self.lista_adjacencia[vertice]}")

    def mostrar_vizinhos(self, vertice):
        if vertice in self.lista_adjacencia:
            print(f"Vizinhos de {vertice}: {self.lista_adjacencia[vertice]}")
        else:
            print(f"O vértice {vertice} não existe no grafo.")

    def bfs(self, inicio):
        visitados = set()
        fila = [inicio]

        while fila:
            vertice = fila.pop(0)
            if vertice not in visitados:
                print(vertice, end=" ")
                visitados.add(vertice)
                fila.extend(self.lista_adjacencia[vertice])

    def dfs_recursivo(self, vertice, visitados=None):
        if visitados is None:
            visitados = set()

        print(vertice, end=" ")
        visitados.add(vertice)

        for vizinho in self.lista_adjacencia[vertice]:
            if vizinho not in visitados:
                self.dfs_recursivo(vizinho, visitados)

grafo = Grafo()

for v in [1, 2, 3, 4, 5, 6]:
    grafo.adicionar_vertice(v)

arestas = [(1, 2), (1, 3), (2, 4), (3, 5), (4, 6), (5, 6)]
for v1, v2 in arestas:
    grafo.adicionar_aresta(v1, v2)

print("Lista de Adjacência do Grafo:")
grafo.mostrar_grafo()

grafo.mostrar_vizinhos(2)

grafo.bfs(1)
print()
grafo.dfs_recursivo(1)
