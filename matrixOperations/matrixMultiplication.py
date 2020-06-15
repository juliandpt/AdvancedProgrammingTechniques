def mulMatrix(matrix0: list, matrix1: list) -> list:
    matrixMul = [[0 for _ in range(len(matrix0))] for _ in range(len(matrix1))]
    for i in range(len(matrix0)):
        for j in range(len(matrix1)):
            for k in range(len(matrix1)):
                matrixMul[i][j] += matrix0[i][k] * matrix1[k][j]
    return matrixMul