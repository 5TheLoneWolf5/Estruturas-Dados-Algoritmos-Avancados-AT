"""

Respostas:

O sistema pode priorizar transações que envolvem múltiplas instuições financeiras por analisar grafos de transação com um maior número de arestas e ligações (entre contas) e assim, analisar possíveis ciclos.

Assim que um ciclo suspeito é detectado, algumas das medidas que podem ser tomadas é a implementação de uma funcionalidade de notificação para os departamentos responsáveis do banco e também o possível bloqueio da conta em questão.

"""

class Grafo:
    def __init__(self):
        self.lista_adjacencia = {}

    def adicionar_vertice(self, vertice):
        if vertice not in self.lista_adjacencia:
            self.lista_adjacencia[vertice] = []

    def adicionar_aresta(self, vertice1, vertice2):
        self.lista_adjacencia[vertice1].append(vertice2)
        self.lista_adjacencia[vertice2].append(vertice1)

    def dfs_recursivo(self, vertice, visitados=None):
        if visitados is None:
            visitados = set()

        print(vertice, end=" ")
        visitados.add(vertice)

        for vizinho in self.lista_adjacencia[vertice]:
            if vizinho not in visitados:
                self.dfs_recursivo(vizinho, visitados)

grafo = Grafo()
vertices = ["Conta A", "Conta B", "Conta C", "Conta D"]
for v in vertices:
    grafo.adicionar_vertice(v)

arestas = [("Conta A", "Conta B"), ("Conta A", "Conta C"), ("Conta B", "Conta D"), ("Conta D", "Conta A"), ("Conta D", "Conta C")]
for v1, v2 in arestas:
    grafo.adicionar_aresta(v1, v2)

print("Busca em Profundidade (DFS) iniciando em Conta A:")
grafo.dfs_recursivo("Conta A")
