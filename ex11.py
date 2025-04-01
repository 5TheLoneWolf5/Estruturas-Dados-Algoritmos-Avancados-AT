"""

- Relatório (tempo):

Tempo para tabuleiro de tamanho 5: 0.000598907470703125 (Menor Grau).
Tempo para tabuleiro de tamanho 8: 0.0010838508605957031 (Menor Grau).
Tempo para tabuleiro de tamanho 10: 0.0013260841369628906 (Menor Grau).

Tempo para tabuleiro de tamanho 5: 0.012674093246459961 (Força Bruta).
Tempo para tabuleiro de tamanho 8: 11.726862907409668 (Força Bruta).
Para o tabuleiro de tamanho 10, não foi possível obter o tempo de execução (o computador não foi capaz de processar a tempo).

Como é possível observar, o algoritmo com base na heurística de Warnsdorff (Menor Grau), se sai melhor comparado em performance comparado a abordagem de força bruta, especialmente em tabuleiros maiores.

"""

import random
import time

def problema_cavalo_menor_grau(n):
    movimentos = [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2)
    ]

    def dentro_tabuleiro(x, y, N):
        return 0 <= x < N and 0 <= y < N

    def movimentos_possiveis(tabuleiro, x, y, N):
        moves = []
        for dx, dy in movimentos:
            nx, ny = x + dx, y + dy
            if dentro_tabuleiro(nx, ny, N) and tabuleiro[nx][ny] == -1:
                moves.append((nx, ny))
        return moves

    def proximo_movimento(tabuleiro, x, y, N):
        moves = movimentos_possiveis(tabuleiro, x, y, N)
        if not moves:
            return None

        moves.sort(key=lambda move: len(movimentos_possiveis(tabuleiro, move[0], move[1], N)))
        
        return moves[0]

    def passeio_do_cavalo(N, inicio_x=0, inicio_y=0):
        tabuleiro = [[-1] * N for _ in range(N)]
        x, y = inicio_x, inicio_y
        tabuleiro[x][y] = 0

        for i in range(1, N * N):
            movimento = proximo_movimento(tabuleiro, x, y, N)
            if not movimento:
                print("Falha: Caminho interrompido!")
                return None
            
            x, y = movimento
            tabuleiro[x][y] = i

        return tabuleiro

    def imprimir_tabuleiro(tabuleiro):
        for linha in tabuleiro:
            print(" ".join(f"{num:2}" for num in linha))

    solucao = passeio_do_cavalo(n)

    if solucao:
        print("\nPasseio do Cavalo encontrado:")
        imprimir_tabuleiro(solucao)

def problema_cavalo_forca_bruta(n):
    def isSafe(x, y, board):
        if(x >= 0 and y >= 0 and x < n and y < n and board[x][y] == -1):
            return True
        return False

    def printSolution(n, board):
        for i in range(n):
            for j in range(n):
                print(board[i][j], end=' ')
            print()

    def solveKT(n):
        board = [[-1 for i in range(n)]for i in range(n)]

        move_x = [2, 1, -1, -2, -2, -1, 1, 2]
        move_y = [1, 2, 2, 1, -1, -2, -2, -1]

        board[0][0] = 0

        pos = 1

        if(not solveKTUtil(n, board, 0, 0, move_x, move_y, pos)):
            print("Solution does not exist")
        else:
            printSolution(n, board)

    def solveKTUtil(n, board, curr_x, curr_y, move_x, move_y, pos):
        if(pos == n**2):
            return True

        for i in range(8):
            new_x = curr_x + move_x[i]
            new_y = curr_y + move_y[i]
            if(isSafe(new_x, new_y, board)):
                board[new_x][new_y] = pos
                if(solveKTUtil(n, board, new_x, new_y, move_x, move_y, pos+1)):
                    return True

                board[new_x][new_y] = -1
        return False

    solveKT(n)

n1 = 5
n2 = 8
n3 = 10

###

start = time.time()
problema_cavalo_menor_grau(n1)
end = time.time()
print(f"Tempo para tabuleiro de tamanho {n1}: {end - start} (Menor Grau).")

###

start = time.time()
problema_cavalo_menor_grau(n2)
end = time.time()
print(f"Tempo para tabuleiro de tamanho {n2}: {end - start} (Menor Grau).")

###

start = time.time()
problema_cavalo_menor_grau(n3)
end = time.time()
print(f"Tempo para tabuleiro de tamanho {n3}: {end - start} (Menor Grau).")

print("--------------------------")

start = time.time()
problema_cavalo_forca_bruta(n1)
end = time.time()
print(f"Tempo para tabuleiro de tamanho {n1}: {end - start} (Força Bruta).")

###

start = time.time()
problema_cavalo_forca_bruta(n2)
end = time.time()
print(f"Tempo para tabuleiro de tamanho {n2}: {end - start} (Força Bruta).")

###

start = time.time()
problema_cavalo_forca_bruta(n3)
end = time.time()
print(f"Tempo para tabuleiro de tamanho {n3}: {end - start} (Força Bruta).")