"""

- Respostas:

* Rota ótima e custo total: F->D->B->CD e 15km.

a. Sim, ele encontrou exatamente o caminho esperado. A rota mais curta do Centro de Distribuição até o Bairro F é 15 km.

b. Essa abordagem pode ser utilizada em cidades maiores (para otimizar a logística) por eficientemente obter os caminhos mais curtos entre o lugar escolhido até outros diversos vértices presentes e 
também por acomodar estruturas maiores e mais complexas com o objetivo de mapear lugares e trajetos.

c. Apesar de houver uma mudança no tipo da unidade, a solução pode se manter a mesma levando em conta o princípio algoritmo procurar o caminho mais curto. 
Contudo, o tempo de viagem pode levar em consideração outras variáveis como o trânsito e acidentes, neste caso, alterando o parâmetro de peso daquela aresta.
Ou seja, dependendo de como a funcionalidade seja de fato implementada, o resultado final pode ser diferente.
É importante deixar claro que o algoritmo de Dijkstra se preocupa com a relação entre os pesos, desde que sejam equivalentes, e não com unidades em específico (15km ou 15m serão vistos do mesmo modo).

"""

class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size

    def add_edge(self, u, v, weight):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = weight
            self.adj_matrix[v][u] = weight 

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    def dijkstra(self, start_vertex_data):
        start_vertex = self.vertex_data.index(start_vertex_data)
        distances = [float('inf')] * self.size
        predecessors = [None] * self.size
        distances[start_vertex] = 0
        visited = [False] * self.size

        for _ in range(self.size):
            min_distance = float('inf')
            u = None
            for i in range(self.size):
                if not visited[i] and distances[i] < min_distance:
                    min_distance = distances[i]
                    u = i

            if u is None:
                break

            visited[u] = True

            for v in range(self.size):
                if self.adj_matrix[u][v] != 0 and not visited[v]:
                    alt = distances[u] + self.adj_matrix[u][v]
                    if alt < distances[v]:
                        distances[v] = alt
                        predecessors[v] = u

        return distances, predecessors

    def get_path(self, predecessors, start_vertex, end_vertex):
        path = []
        current = self.vertex_data.index(end_vertex)
        while current is not None:
            path.insert(0, self.vertex_data[current])
            current = predecessors[current]
            if current == self.vertex_data.index(start_vertex):
                path.insert(0, start_vertex)
                break
        return '->'.join(path)

g = Graph(7)

g.add_vertex_data(0, 'CD')
g.add_vertex_data(1, 'A')
g.add_vertex_data(2, 'B')
g.add_vertex_data(3, 'C')
g.add_vertex_data(4, 'D')
g.add_vertex_data(5, 'E')
g.add_vertex_data(6, 'F')

g.add_edge(0, 1, 4)
g.add_edge(0, 2, 2)
g.add_edge(1, 3, 5)
g.add_edge(1, 4, 10)
g.add_edge(2, 1, 3)
g.add_edge(2, 4, 8)
g.add_edge(3, 4, 2)
g.add_edge(3, 5, 4)
g.add_edge(4, 5, 6)
g.add_edge(4, 6, 5)
g.add_edge(5, 6, 3)

print("\nAlgoritmo de Dijkstra\n")
dis, pred = g.dijkstra('F')

print("Caminho:  |  Distância:")

for i, d in enumerate(dis):
    _path = g.get_path(pred, 'F', g.vertex_data[i])
    print(f"{_path} {d}km")