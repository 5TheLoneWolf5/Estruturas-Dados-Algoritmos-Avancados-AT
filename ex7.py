"""

- Grafo:

Cidades (Vértices): A, B, C, D, E, F
Estradas (Arestas):

A ↔ B
A ↔ C
B ↔ D
C ↔ E
D ↔ F

Resposta:

Para este caso, uma Lista de Adjacência é uma opção mais eficiente para armazenar este conjunto de dados, já que cada vértice dentro da estrutura possui apenas duas conexões, fazendo deste um grafo não denso.
Um grafo denso seria um grafo com o número de arestas próximo ou igual ao número possível de arestas entre os vértices.

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

grafo = Grafo()

for v in ["A", "B", "C", "D", "E", "F"]:
    grafo.adicionar_vertice(v)

arestas = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "E"), ("D", "F"), ("E", "F")]
for v1, v2 in arestas:
    grafo.adicionar_aresta(v1, v2)

print("Lista de Adjacência do Grafo:")
grafo.mostrar_grafo()
