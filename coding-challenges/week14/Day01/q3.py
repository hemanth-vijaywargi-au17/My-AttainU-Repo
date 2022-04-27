'''
Q-3) Find Center of Star Graph (5 marks)
https://leetcode.com/problems/find-center-of-star-graph/
(Easy)
There is an undirected star graph consisting of n nodes labeled from 1 to n. A
star graph is a graph where there is one center node and exactly n - 1 edges that
connect the center node with every other node.
You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates
that there is an edge between the nodes ui and vi. Return the center of the given
star graph.
'''

dict={}
edges = [[1,2],[2,3],[4,2]]
for i in range(len(edges)):
    for j in range(len(edges[0])):
        if edges[i][j] not in dict:
            dict[edges[i][j]]=[]
        if j==0:
            dict[edges[i][j]].append(edges[i][j+1])
        else:
            dict[edges[i][j]].append(edges[i][j-1])
            
a=len(dict)
for key,value in dict.items():
    if len(value) == len(dict)-1:
        print(key)