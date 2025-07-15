# Graph Representation

# Edge List
n = 8 # number of nodes

edge_list = [[0,1], [0,3], [1,2], [3,4], [3,6], [3,7], [4,2], [4,5], [5,2]] # list of edges

print(edge_list) # print the edges list

# Adjacency Matrix
adjacency_matrix = []

for row in range(0,n):
    adjacency_matrix.append([0]*n) # creating 2d matrix
    
for start_node, end_node in edge_list:
    # for directed graph
    adjacency_matrix[start_node][end_node] = 1 # creating edge between nodes
    
    # for undirected graph
    # adjacency_matrix[end_node][start_node] = 1 # reverse connection or 2 way connection for undirected graph

for row in range(0,n):
    print(f"{row} = ", adjacency_matrix[row]) # print the 2d matrix

# Ajacency List
from collections import defaultdict

adjacency_list = defaultdict(list)

for start_node, end_node in edge_list:
    adjacency_list[start_node].append(end_node) # for directed graph
    adjacency_list[end_node].append(start_node) # for undirected graph
    
for node in adjacency_list:
    print(f"{node} = ", adjacency_list[node]) # print adjacency_list
    
print(adjacency_list) # print adjacency_list
    
# print the list of neighboring nodes for a node
for node in adjacency_list:
    print(f"{node} : {adjacency_list[node]}")

