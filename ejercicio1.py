laberinto = [
    [1, 1, 1, 1, 99, 1, 1, 1, 0],   
    [1, 99, 1, 1, 99, 1, 1, 1, 99],
    [1, 1, 99, 1, 1, 1, 1, 1, 99],
    [99, 1, 1, 99, 1, 99, 99, 1, 99],
    [1, 1, 99, -1, 1, 1, 1, 3, 99],
    [-2, 99, 1, 99, 1, 99, 1, 1, 1],
    [1, 1, 99, -1, 1, 1, 1, 1, 99],
    [1, 99, 99, 99, 1, 2, 1, 1, 99],
    [0, 1, 3, 1, 1, 1, 99, 1, 1]  
]

inicio = (0, 8)

fin = (8, 0)

movimientos = [ (0,-1), (1,0), (-1,0), (0,1) ]

def mostrar_matriz(m):
    for fila in m:
        print(fila)
    print()

def backtracking(x, y, energia, visitado, camino):
    if energia < 0:
        return False

    if (x, y) == fin:
        return True

    for dx, dy in movimientos:
        nx, ny = x + dx, y + dy

        if 0 <= nx < 9 and 0 <= ny < 9:

            if (nx, ny) in visitado:
                continue

            valor = laberinto[nx][ny]

            if valor == 99:
                continue

            nueva_energia = energia
            if valor > 0:
                nueva_energia -= valor
            elif valor < 0:
                nueva_energia -= valor

            visitado.add((nx, ny))
            camino.append((nx, ny))

            if backtracking(nx, ny, nueva_energia, visitado, camino):
                return True

            visitado.remove((nx, ny))
            camino.pop()

    return False


def resolver_camino():
    print("*****LABERINTO ORIGINAL*****")
    mostrar_matriz(laberinto)

    energia_inicial = 18
    visitado = set([inicio])
    camino = [inicio]

    if backtracking(inicio[0], inicio[1], energia_inicial, visitado, camino):
        print("Encontramos un camino mi King, Energía inicial:", energia_inicial)

        matriz_camino = [[" " for _ in range(9)] for _ in range(9)]
        for (i, j) in camino:
            matriz_camino[i][j] = "*"

        matriz_camino[inicio[0]][inicio[1]] = "I"
        matriz_camino[fin[0]][fin[1]] = "F"

        print("\n*****CAMINO ENCONTRADO*****")
        mostrar_matriz(matriz_camino)

    else:
        print("Sorry no fue posible llegar a la meta mi brou")


resolver_camino()
