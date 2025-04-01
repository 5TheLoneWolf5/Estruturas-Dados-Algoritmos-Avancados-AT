"""

- Comparação dos tempos de execução e resultados:

---------------------------------------------

80
Tempo para Programação Dinâmica: 1.6927719116210938e-05.

---------------------------------------------

Custo mínimo : 80
Tempo para Heurística Gulosa: 6.723403930664062e-05.

---------------------------------------------

População inicial:
GNOME     VALOR FITNESS

02130 95
02130 95
02130 95
02130 95
02130 95
02130 95
02130 95
02130 95
02130 95
02130 95


Atual:  10000
Geração 1
GNOME     VALOR FITNESS
01230 95
01230 95
02310 80
01230 95
01230 95
02310 80
01230 95
01230 95
03120 95
03120 95

Atual:  9000.0
Geração 2
GNOME     VALOR FITNESS
01320 80
01320 80
03210 95
01320 80
02130 95
02130 95
02130 95
03210 95
01320 80
03210 95

Atual:  8100.0
Geração 3
GNOME     VALOR FITNESS
01230 95
03120 95
01230 95
01230 95
02310 80
02310 80
01230 95
01230 95
01230 95
02310 80

Atual:  7290.0
Geração 4
GNOME     VALOR FITNESS
02130 95
03210 95
03210 95
03210 95
01320 80
03210 95
01320 80
03210 95
03210 95
01320 80

Atual:  6561.0
Geração 5
GNOME     VALOR FITNESS
01230 95
03120 95
03120 95
03120 95
03120 95
01230 95
01230 95
01230 95
02310 80
03120 95
Tempo para Algoritmo Genético: 0.0032835006713867188.

- Análise:

Como é possível analisar, a programação gulosa teve o melhor resultado, com a programação dinâmica logo depois, e então o algoritmo genético.

Pontos a se destacar: 

- A heurística gulosa é rápida e simples, mas não garante encontrar a solução ótima. 
- A programação dinâmica pode ser computacionalmente cara, mas encontra o caminho ótimo.
- Já o algoritmo genético tem uma abordagem de evolução, e oferece boas soluções com datasets maiores.

---------------------------------------------

"""

### Programação Dinâmica ###

import sys
import time
from random import randint
from typing import DefaultDict

def totalCost(mask, pos, n, cost):
    if mask == (1 << n) - 1:
        return cost[pos][0]

    ans = sys.maxsize   

    for i in range(n):
        if (mask & (1 << i)) == 0: 
            ans = min(ans, cost[pos][i] +
                      totalCost(mask | (1 << i), i, n, cost))

    return ans
 

def tsp(cost):
    n = len(cost)
    return totalCost(1, 0, n, cost)

### Heurística Gulosa ###

INT_MAX = 2147483647

def findMinRoute(tsp):
    sum = 0
    counter = 0
    j = 0
    i = 0
    min = INT_MAX
    visitedRouteList = DefaultDict(int)

    visitedRouteList[0] = 1
    route = [0] * len(tsp)

    while i < len(tsp) and j < len(tsp[i]):

        if counter >= len(tsp[i]) - 1:
            break

        if j != i and (visitedRouteList[j] == 0):
            if tsp[i][j] < min:
                min = tsp[i][j]
                route[counter] = j + 1

        j += 1

        if j == len(tsp[i]):
            sum += min
            min = INT_MAX
            visitedRouteList[route[counter] - 1] = 1
            j = 0
            i = route[counter] - 1
            counter += 1

    i = route[counter - 1] - 1

    for j in range(len(tsp)):

        if (i != j) and tsp[i][j] < min:
            min = tsp[i][j]
            route[counter] = j + 1

    sum += min

    print("Custo mínimo :", sum)

### Algoritmo Genético ###

INT_MAX = 2147483647
V = 4
GENES = "ABCD"
START = 0
POP_SIZE = 10

class individual:
    def __init__(self) -> None:
        self.gnome = ""
        self.fitness = 0

    def __lt__(self, other):
        return self.fitness < other.fitness

    def __gt__(self, other):
        return self.fitness > other.fitness

def rand_num(start, end):
    return randint(start, end-1)

def repeat(s, ch):
    for i in range(len(s)):
        if s[i] == ch:
            return True

    return False

def mutatedGene(gnome):
    gnome = list(gnome)
    while True:
        r = rand_num(1, V)
        r1 = rand_num(1, V)
        if r1 != r:
            temp = gnome[r]
            gnome[r] = gnome[r1]
            gnome[r1] = temp
            break
    return ''.join(gnome)

def create_gnome():
    gnome = "0"
    while True:
        if len(gnome) == V:
            gnome += gnome[0]
            break

        temp = rand_num(1, V)
        if not repeat(gnome, chr(temp + 48)):
            gnome += chr(temp + 48)

    return gnome

def cal_fitness(gnome):
    mp = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    f = 0
    for i in range(len(gnome) - 1):
        if mp[ord(gnome[i]) - 48][ord(gnome[i + 1]) - 48] == INT_MAX:
            return INT_MAX
        f += mp[ord(gnome[i]) - 48][ord(gnome[i + 1]) - 48]

    return f

def cooldown(temp):
    return (90 * temp) / 100

def TSPUtil(mp):
    gen = 1
    gen_thres = 5

    population = []
    temp = individual()

    for i in range(POP_SIZE):
        temp.gnome = create_gnome()
        temp.fitness = cal_fitness(temp.gnome)
        population.append(temp)

    print("\nPopulação inicial: \nGNOME     VALOR FITNESS\n")
    for i in range(POP_SIZE):
        print(population[i].gnome, population[i].fitness)
    print()

    found = False
    temperature = 10000

    while temperature > 1000 and gen <= gen_thres:
        population.sort()
        print("\nAtual: ", temperature)
        new_population = []

        for i in range(POP_SIZE):
            p1 = population[i]

            while True:
                new_g = mutatedGene(p1.gnome)
                new_gnome = individual()
                new_gnome.gnome = new_g
                new_gnome.fitness = cal_fitness(new_gnome.gnome)

                if new_gnome.fitness <= population[i].fitness:
                    new_population.append(new_gnome)
                    break

                else:
                    prob = pow(
                        2.7,
                        -1
                        * (
                            (float)(new_gnome.fitness - population[i].fitness)
                            / temperature
                        ),
                    )
                    if prob > 0.5:
                        new_population.append(new_gnome)
                        break

        temperature = cooldown(temperature)
        population = new_population
        print("Geração", gen)
        print("GNOME     VALOR FITNESS")

        for i in range(POP_SIZE):
            print(population[i].gnome, population[i].fitness)
        gen += 1


if __name__ == "__main__":

    print("---------------------------------------------")
    
    cost = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    start = time.time()
    result = tsp(cost)
    end = time.time()
    print(result)
    print(f"Tempo para Programação Dinâmica: {end - start}.")

    print("---------------------------------------------")

    tsp = [
        [-1, 10, 15, 20], 
        [10, -1, 35, 25], 
        [15, 35, -1, 30], 
        [20, 25, 30, -1]
    ]

    start = time.time()
    findMinRoute(tsp)
    end = time.time()
    print(f"Tempo para Heurística Gulosa: {end - start}.")

    print("---------------------------------------------")

    mp = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    start = time.time()
    TSPUtil(mp)
    end = time.time()
    print(f"Tempo para Algoritmo Genético: {end - start}.")

    print("---------------------------------------------")