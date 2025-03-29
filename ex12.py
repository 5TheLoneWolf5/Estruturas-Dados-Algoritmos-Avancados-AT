"""

No código abaixo, utilizo BFS para encontrar o caminho mais curto entre o bairro A e o bairro F. Também é retornado o caminho e bairros percorridos.

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

    def mostrar_grafo(self):
        for vertice in self.lista_adjacencia:
            print(f"{vertice} -> {self.lista_adjacencia[vertice]}")

    def mostrar_vizinhos(self, vertice):
        if vertice in self.lista_adjacencia:
            print(f"Vizinhos de {vertice}: {self.lista_adjacencia[vertice]}")
        else:
            print(f"O vértice {vertice} não existe no grafo.")

    def bfs(self, inicio, objetivo):
        visitados = set()
        fila = [inicio]

        while fila:
            vertice = fila.pop(0)
            if vertice not in visitados:
                print(vertice, end=" ")
                if vertice == objetivo:
                    print(f"\n{objetivo} encontrado!")
                    return visitados
                visitados.add(vertice)
                fila.extend(self.lista_adjacencia[vertice])
        
grafo = Grafo()

for v in ["A", "B", "C", "D", "E", "F"]:
    grafo.adicionar_vertice(v)

arestas = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("F", "C")]
for v1, v2 in arestas:
    grafo.adicionar_aresta(v1, v2)

print("Lista de Adjacência do Grafo:")
grafo.mostrar_grafo()

grafo.bfs("A", "C")
