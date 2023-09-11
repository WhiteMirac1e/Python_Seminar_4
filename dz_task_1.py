# ✔ Напишите функцию для транспонирования матрицы
def matrix_t(matrix):
    result =[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])): 
            result[j][i] = matrix[i][j] 
    return result

def show_matrix(matrix):
    for i in matrix:
        for j in i:
            print(j, end=' ')
        print()

arr = [[2, 5, 7], [1, 2, 3], [4, 5, 6]] 
arr2 = matrix_t(arr)
print(show_matrix(arr2))
