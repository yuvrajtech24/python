# Graph Representation

# Edge List
edge_list = [
    [0,1],
    [1,2],
    [0,3],
    [3,4],
    [3,6],
    [3,7],
    [4,2],
    [4,5],
    [5,2]
]

# Adjacency Matrix
matrix = []
n = 8
for i in range(0,n):
    matrix.append([0]*n)
    
for u,v in edge_list:
    matrix[u][v] = 1
    
for i in range(0,n):
    print(matrix[i])

# Adjacency List
from collections import defaultdict

adjacency_list = defaultdict(list)

for u,v in edge_list:
    adjacency_list[u].append(v)
    
for i in adjacency_list:
    print(f"{i} : {adjacency_list[i]}")

# Class Based
