# n и edge_list, видимо, считывать не надо, они уже существуют? или это логическое продолжение первого задания?
# граф считаю ориентированным, вершины нумерую с нуля

def edge_list_to_adj_matrix(edge_list, n):
    adj_matrix = [[0 for i in range(n)] for j in range(n)]
    for edge in edge_list:
        adj_matrix[edge[0]][edge[1]]=1