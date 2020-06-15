def sumMatrix(matrix0: list, matrix1: list) -> list:
    matrixSum = [[0 for _ in range(len(matrix0))] for _ in range(len(matrix1))]
    for i in range(len(matrix0)):
        for j in range(len(matrix1)):
            matrixSum[i][j] = matrix0[i][j] + matrix1[i][j]
    return matrixSum