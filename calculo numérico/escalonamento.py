def get_scalon(matrix: list) -> list:
    for i in range(len(matrix)):
        if matrix[i][i] == 0:
            for j in range(i + 1, len(matrix)):
                if matrix[j][i] != 0:
                    matrix[i], matrix[j] = matrix[j], matrix[i]
                    break
        for j in range(i + 1, len(matrix)):
            if matrix[j][i] != 0:
                matrix[j] = [
                    round(matrix[j][k] - matrix[i][k] * matrix[j][i] / matrix[i][i], 2)
                    for k in range(len(matrix[j]))
                ]
    return matrix


def show_matriz(matriz):
    """mostra a matriz na tela de maneira agradável"""
    print("\n\n")
    for i, l in enumerate(matriz):
        for e in l:
            print(e, end="  ")
        print("\n\n")


for x in range(3):
    main_matrix = [
        [2 * x, -1 * x, 0, 0, 0, 0],
        [-1 * x, 2 * x, -1 * x, 0, 0, 0],
        [0, -1 * x, 2 * x, -1 * x, 0, 0],
        [0, 0, -1 * x, 2 * x, -1 * x, 0],
        [0, 0, 0, -1 * x, 2 * x, -1 * x],
        [0, 0, 0, 0, -1 * x, 2 * x],
    ]
    show_matriz(get_scalon(main_matrix))
