def is_square_matrix_of_n(matrix, row, col, n_matrix_square):
    symbols_in_matrix = []
    if 0 <= row < len(matrix)  and 0 <= col < len(matrix[0]):
        for i in range(row,row + n_matrix_square):
            for j in range(col, col + n_matrix_square):
                current_symbol = matrix[i][j]
                symbols_in_matrix.append(current_symbol)
    is_square_matrix = True
    for i in range(len(symbols_in_matrix)-1):
        if symbols_in_matrix[i+ 1]  != symbols_in_matrix[i]:
            is_square_matrix = False
    return is_square_matrix



row, col = [int(x) for x in input().split(' ')]
n = int(input())

matrix = []

for i in range(row):
    matrix.append(input().split(' '))
sum_matrix = 0
for i in range(len(matrix)-n+1):
    for j in range(len(matrix[0])-n+1):
        if is_square_matrix_of_n(matrix, i, j, n):
            sum_matrix += 1

print(sum_matrix)
