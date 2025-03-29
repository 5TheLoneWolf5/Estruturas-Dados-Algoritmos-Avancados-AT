"""

- Resultado:

Caminho até chegar em E: ['A', 'C', 'E']. Custo: 9.

- Comparação de desempenho:

No quesito de desempenho e memória, a lista de adjacência se sai melhor do que a matriz de adjacência. Isso porque durante a travesia do algoritmo BFS, uma estrutura de matriz de adjacência sempre
precisa iterar uma quantidade de arestas igual ao número de vértices, afetando a complexidade e o desempenho e memória do programa.

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

centros = ["A", "B", "C", "D", "E"]

for c in centros:
    grafo.adicionar_vertice(c)

arestas = [("A", "B", 2), ("A", "C", 4), ("B", "D", 1), ("C", "E", 5), ("D", "E", 3)]

for v1, v2, p in arestas:
    grafo.adicionar_aresta(v1, v2, p)

print("Lista de Adjacência do Grafo:")
grafo.mostrar_grafo()

print("Lista de Vizinhos:")
for c in centros:
    grafo.mostrar_vizinhos(c)

print("Encontrando rota mais curta entre A e E com BFS: ")
resultado = grafo.bfs("A", "E")
print(resultado)
