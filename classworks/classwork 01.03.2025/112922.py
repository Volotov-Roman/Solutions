def DFS(curr_node, adj_list, visited=None):
    if visited is None:
        visited = set()
    visited.add(curr_node)
    for adj_node in adj_list[curr_node]:
        if adj_node not in visited:
            DFS(adj_node, adj_list, visited)
    return visited

def connect_comp(start_node, adj_list):
    fd_set = DFS(start_node, adj_list)
    return fd_set

def edge_list_to_adj_list(edge_list, size):
    adj_list=[[] for i in range(size)]
    for edge in edge_list:
        adj_list[edge[0]-1].append(edge[1]-1)
        adj_list[edge[1]-1].append(edge[0]-1)
    return adj_list

def len_check(adj_list, atomstring, size):
    for i in range(size):
        if (atomstring[i]=='H' and len(adj_list[i])!=1) or (atomstring[i]=='C' and len(adj_list[i])!=4):
            return False
    return True

n, m = map(int, input().split())
atomstring = list(input())
edge_list = [input().split() for i in range(m)]
for i in range(m):
    for j in range(2):
        edge_list[i][j] = int(edge_list[i][j])
adj_list = edge_list_to_adj_list(edge_list, n)
if (m==0) or (connect_comp(0, adj_list) != set([i for i in range(n)])) or (not len_check(adj_list, atomstring, n)):
    print('NO')
else:
    print('YES')

