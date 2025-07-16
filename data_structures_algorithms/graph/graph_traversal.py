# Graph Representation

# Edge List
n = 8 # number of nodes

edge_list = [[0,1], [0,3], [1,2], [3,4], [3,6], [3,7], [4,2], [4,5], [5,2]] # list of edges

print(edge_list) # print the edges list

# Adjacency List
from collections import defaultdict, deque

adjacency_list = defaultdict(list)

for start_node, end_node in edge_list:
    adjacency_list[start_node].append(end_node) # for directed graph
    # adjacency_list[end_node].append(start_node) # for undirected graph
    
for node in adjacency_list:
    print(f"{node} = ", adjacency_list[node]) # print adjacency_list
    
print(adjacency_list) # print adjacency_list
    
# print the list of neighboring nodes for a node
for node in adjacency_list:
    print(f"{node} : {adjacency_list[node]}")

# Graph Traversal

# DFS
source_node = 0

def dfs_recursive_traversal(node):
    visited_nodes = set()
    # display the node
    # add it to the visited_node
    # for each neighboring node:
        # if the adjacent node is not in visited nodes list
            # visit that node recursively
        # else, skip the current adjacent node
    
    print(node)
    visited_nodes.add(node)
    for neighbor_node in adjacency_list[node]:
        if(neighbor_node not in visited_nodes):
            dfs_recursive_traversal(neighbor_node)
            
# dfs_recursive_traversal(source_node)

# BFS
def bfs_traversal(node):
    # add the first node to the queue
    # mark it visited
    # while the queue is not empty
        # dequeue the left most element
        # for each neighbor node
            # if neighbor node not visited
                # add neighbor node to queue
                # mark neighbor node as visited
                
    q = deque()
    visited_nodes = set()
    start_node = node
    
    q.append(start_node)
    visited_nodes.add(start_node)
    while q:
        visited_node = q.popleft()
        print(visited_node)
        for neighbor_node in adjacency_list[visited_node]:
            if (neighbor_node not in visited_nodes):
                q.append(neighbor_node)
                visited_nodes.add(neighbor_node)
    
bfs_traversal(source_node)