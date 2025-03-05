colour = ['white' for i in range(n)]
def DPDFS(adj_list, start_node):
    colour[start_node]='gray'
    print(start_node)
    for neighbour in adj_list[start_node]:
        if colour[neighbour]=='white':
            DPDFS(adj_list, neighbour)
    print(start_node)
    colour[start_node]='black'