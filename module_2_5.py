def get_matrix(n, m, value):
    matrix = []
    for strings in range(n):
        matrix.append([])
        for columns in range(m):
            matrix[strings].append(value)
    print(matrix)


result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
