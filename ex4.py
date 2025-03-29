"""

Resultado:

Lista de Adjacência do Grafo:
Centro -> ['Bairro A', 'Bairro B']
Bairro A -> ['Centro', 'Bairro C']
Bairro B -> ['Centro', 'Bairro C']
Bairro C -> ['Bairro A', 'Bairro B', 'Bairro D']
Bairro D -> ['Bairro C']
Vizinhos de Bairro C: ['Bairro A', 'Bairro B', 'Bairro D']

Resposta:

A lista de adjacência otimiza o armazenamento das conexões comparado à matriz de adjacência pois a matriz de adjacência necessita de espaços para representar todas as conexões entre cada vértice dentro de cada vértice na matriz,
independentemente se o vértice em questão possui uma relação existente ou não (os valores sendo representados por 0 ou 1). De forma diferente, a lista de adjacência armazena apenas os valores existentes, portanto, sendo mais eficiente no armazenamento de um grafo com poucas arestas.

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
        """Exibe os vizinhos de um determinado vértice"""
        if vertice in self.lista_adjacencia:
            print(f"Vizinhos de {vertice}: {self.lista_adjacencia[vertice]}")
        else:
            print(f"O vértice {vertice} não existe no grafo.")

grafo = Grafo()

for v in ["Centro", "Bairro A", "Bairro B", "Bairro C", "Bairro D"]:
    grafo.adicionar_vertice(v)

arestas = [("Centro", "Bairro A"), ("Centro", "Bairro B"), ("Bairro A", "Bairro C"), ("Bairro B", "Bairro C"), ("Bairro C", "Bairro D")]
for v1, v2 in arestas:
    grafo.adicionar_aresta(v1, v2)

print("Lista de Adjacência do Grafo:")
grafo.mostrar_grafo()

grafo.mostrar_vizinhos("Bairro C")
