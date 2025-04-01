"""

Respostas:



Caso a situação envolva armazenar e processar grandes cidades com milhares de bairros e conexões, a matriz de adjacência se sai melhor por ser mais eficiente em grafos densos.

"""

class Grafo:
    def __init__(self):
        self.lista_adjacencia = {}

    def adicionar_vertice(self, vertice):
        if vertice not in self.lista_adjacencia:
            self.lista_adjacencia[vertice] = []

    def adicionar_aresta(self, vertice1, vertice2, peso):
        if vertice1 in self.lista_adjacencia and vertice2 in self.lista_adjacencia:
            self.lista_adjacencia[vertice1].append((vertice2, peso))
            self.lista_adjacencia[vertice2].append((vertice1, peso))
            
    def mostrar_grafo(self):
        for vertice in self.lista_adjacencia:
            print(f"{vertice} -> {self.lista_adjacencia[vertice]}")

    def mostrar_vizinhos(self, vertice):
        if vertice in self.lista_adjacencia:
            print(f"Vizinhos de {vertice}: {self.lista_adjacencia[vertice]}")
        else:
            print(f"O vértice {vertice} não existe no grafo.")

    def bfs(self, vertice1, vertice2):
        visitados = set()
        fila = [(0, vertice1, [])]
        
        while fila:
            c, v, p = fila.pop(0)
            
            if v in visitados:
                continue

            p = p + [v]
            visitados.add(v)
            
            if v == vertice2:
                return (f"Caminho até chegar em {vertice2}: {p}. Custo: {c}.")
            
            for vizinho, peso in self.lista_adjacencia[v]:
                if vizinho not in visitados:
                    print(vizinho)
                    fila.append((c + peso, vizinho, p))

        return float("inf")

grafo = Grafo()

centros = ["A", "B", "C", "D", "E", "F"]

for c in centros:
    grafo.adicionar_vertice(c)

arestas = [("A", "B", 4), ("A", "C", 2), ("B", "D", 5), ("C", "E", 3), ("C", "D", 8), ("D", "F", 6), ("E", "F", 1)]

for v1, v2, p in arestas:
    grafo.adicionar_aresta(v1, v2, p)

print("Lista de Adjacência do Grafo:")
grafo.mostrar_grafo()

print("Lista de Vizinhos:")
for c in centros:
    grafo.mostrar_vizinhos(c)

####################################################################################################

class GrafoMatriz:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.matriz = [[0] * num_vertices for _ in range(num_vertices)]
        self.vertices = {}
        self.indice_para_vertice = {}
        self.contador = 0
        
    def adicionar_vertice(self, vertice):
        if vertice not in self.vertices and self.contador < self.num_vertices:
            self.vertices[vertice] = self.contador
            self.indice_para_vertice[self.contador] = vertice
            self.contador += 1

    def adicionar_aresta(self, vertice1, vertice2, w):
        if vertice1 in self.vertices and vertice2 in self.vertices:
            i, j = self.vertices[vertice1], self.vertices[vertice2]
            self.matriz[i][j] = w
            self.matriz[j][i] = w

    def mostrar_matriz(self):
        print("Matriz de Adjacência:")
        print("  ", "  ".join(self.vertices.keys()))
        for i, linha in enumerate(self.matriz):
            print(self.indice_para_vertice[i], linha)

    def mostrar_vizinhos(self, vertice):
        if vertice in self.vertices:
            indice = self.vertices[vertice]
            vizinhos = [self.indice_para_vertice[i] for i in range(self.num_vertices) if self.matriz[indice][i] > 0]
            print(f"Vizinhos de {vertice}: {vizinhos}")
        else:
            print(f"O vértice {vertice} não existe no grafo.")

grafoMatriz = GrafoMatriz(6)

for v in ["A", "B", "C", "D", "E", "F"]:
    grafoMatriz.adicionar_vertice(v)

arestas = [("A", "B", 4), ("A", "C", 2), ("B", "D", 5), ("C", "E", 3), ("C", "D", 8), ("D", "F", 6), ("E", "F", 1)]
for v1, v2, w in arestas:
    grafoMatriz.adicionar_aresta(v1, v2, w)

grafoMatriz.mostrar_matriz()
