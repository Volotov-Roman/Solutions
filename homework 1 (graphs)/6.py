# без n-ного запуска
# edge = [node_1, node_2, weight]

def Ford_Bellman(edge_list, n, start_node):
    dist=[float('inf') for i in range(n)]
    dist[start_node]=0
    for i in range(n-1):
        for edge in edge_list:
            dist[edge[1]]=min(dist[edge[1]], dist[edge][0]+edge[2])
    return dist