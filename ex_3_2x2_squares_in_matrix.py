def is_square_matrix_of_2(mat, r, c):
    if 0 <= r < len(mat) - 1 and 0 <= c < len(mat[0]) - 1:
        if mat[r][c] == mat[r][c + 1] == mat[r + 1][c] == mat[r + 1][c + 1]:
            return True


row, col = [int(x) for x in input().split(' ')]

matrix = []

for i in range(row):
    matrix.append(input().split(' '))
sum_matrix = 0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if is_square_matrix_of_2(matrix, i, j):
            sum_matrix += 1

print(sum_matrix)
