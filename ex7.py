"""

Resultado:

-----------------
-1 5 10 -1 -1 -1
5 -1 3 8 -1 -1
10 3 -1 2 7 -1
-1 8 2 -1 4 6
-1 -1 7 4 -1 5
-1 -1 -1 6 5 -1
-----------------
10 5 8 10 14 16
5 6 3 5 9 11
8 3 4 2 6 8
10 5 2 4 4 6
14 9 6 4 8 5
16 11 8 6 5 10
-----------------

Respostas:

a. O tempo mínimo para viajar do Bairro A até o Bairro F é 16.
b. Se uma rua (conexão fechar), isso pode mudar como o algoritmo vai percorrer a estrutura, e resultará nos vértices (com menores tempos) obterem outros caminhos, podendo aumentar o tamanho da distância até o destino.
c. Este método pode ajudar no planejamento de novas linhas de transporte por mapear estações de trem e informar sobre as melhores e menores distâncias entre todos os pontos já na fase de planejamento. Isto poderá melhorar na tomada de decisões,
e também informará os envolvidos com dados, rotas e estações.

"""

def floydWarshall(graph):
    V = len(graph)
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if ((graph[i][j] == -1 or graph[i][j] > (graph[i][k] + graph[k][j])) and (graph[k][j] != -1 and graph[i][k] != -1)):
                    graph[i][j] = graph[i][k] + graph[k][j]

print("-----------------")

grafo_cidade = [
    [-1, 5, 10, -1, -1, -1],
    [5, -1, 3, 8, -1, -1],
    [10, 3, -1, 2, 7, -1],
    [-1, 8, 2, -1, 4, 6],
    [-1, -1, 7, 4, -1, 5],
    [-1, -1, -1, 6, 5, -1],
]

for i in grafo_cidade:
    print(*i)
    
floydWarshall(grafo_cidade)

print("-----------------")

for i in grafo_cidade:
    print(*i)

print("-----------------")