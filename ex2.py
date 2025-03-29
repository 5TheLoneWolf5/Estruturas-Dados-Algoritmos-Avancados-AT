"""

Para este exercício, foi implementado uma Lista de Adjacência.

Justificação:

Se o objetivo for encontrar a rota mais curta entre dois bairros, a Lista de Adjacência com BFS (Breadth-first search) é uma melhor opção por conta da estrutura utilizar menos memória e por guardar apenas as conexões existentes entre os bairros.

"""

class MapaCidade:
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

cidade = MapaCidade()
bairros = ["Centro", "Jardins", "Vila Madalena", "Brooklin", "Moema", "Pinheiros", "Itaim Bibi"]

for i in bairros:
    cidade.adicionar_vertice(i)

ruas = [("Centro", "Jardins"), ("Centro", "Pinheiros"), ("Jardins", "Moema"), ("Moema", "Brooklin"), ("Brooklin", "Itaim Bibi"), ("Pinheiros", "Vila Madalena")]

for i, j in ruas:
    cidade.adicionar_aresta(i, j)

cidade.bfs("Centro")
