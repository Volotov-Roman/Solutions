def transpose(adj_matrix):
    for i in range(len(adj_matrix)):
        for j in range(i):             # идём только по нижнему треугольнику
            adj_matrix[i][j]=adj_matrix[j][i]