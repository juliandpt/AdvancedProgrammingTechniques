size = 9
#Las celdas con un 0 son celdas vacías
matrix = [
    [6,5,0,8,7,3,0,9,0],
    [0,0,3,2,5,0,0,0,8],
    [9,8,0,1,0,4,3,5,7],
    [1,0,5,0,0,0,0,0,0],
    [4,0,0,0,0,0,0,0,2],
    [0,0,0,0,0,0,5,0,3],
    [5,7,8,3,0,1,0,2,6],
    [2,0,0,0,4,8,9,0,0],
    [0,9,0,6,2,5,0,8,1]]

#funcion para imprimir el sudoku
def printSudoku():
    for i in matrix:
        print (i)

#función para verificar si todas las celdas están asignadas o no
#si hay alguna celda no asignada
#entonces esta función cambiará los valores de las columnas y filas en consecuencia
def numberUnassigned(row, col):
    num_unassign = 0
    for i in range(0, size):
        for j in range (0, size):
            #celda no está asignada
            if matrix[i][j] == 0:
                row = i
                col = j
                num_unassign = 1
                a = [row, col, num_unassign]
                return a
    a = [-1, -1, num_unassign]
    return a
#función para verificar si podemos poner un valor en una celda en paticular o no
def isSafe(n, r, c):
    #comprieba en fila
    for i in range(0, size):
        #hay una celda con el mismo valor
        if matrix[r][i] == n:
            return False
    #revisando en columna
    for i in range(0, size):
        #hay una celda con el mismo valor
        if matrix[i][c] == n:
            return False
    row_start = (r//3)*3
    col_start = (c//3)*3
    #revisando submatriz
    for i in range(row_start, row_start+3):
        for j in range(col_start, col_start+3):
            if matrix[i][j]==n:
                return False
    return True

#función para verificar si podemos poner un valor en una celda paticular o no
def solveSudoku():
    row = 0
    col = 0
    #si todas las celdas están asignadas, el sudoku ya está resuelto pasar por la referencia porque number_unassigned cambiará los valores de fila y columna
    a = numberUnassigned(row, col)
    if a[2] == 0:
        return True
    row = a[0]
    col = a[1]
    #numeros entre 1 y 9
    for i in range(1,10):
        #si podemos asignar i a la celda o no
        #la celda es matrix[row][col]
        if isSafe(i, row, col):
            matrix[row][col] = i
            #backtracking
            if solveSudoku():
                return True
            #si no podemos continuar con esta solución, reasigne la celda
            matrix[row][col]=0
    return False

if solveSudoku():
    printSudoku()
else:
    print("No hay solución")