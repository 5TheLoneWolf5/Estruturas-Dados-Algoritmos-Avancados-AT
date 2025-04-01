"""

- Respostas:

Sim, ele encontrou exatamente o caminho esperado:

Essa abordagem pode ser utilizada em cidades maiores.

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

        return distances

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
distances = g.dijkstra('F')

for i, d in enumerate(distances):
    print(f"Distância de F para {g.vertex_data[i]}: {d}")