from sys import stdin
from collections import deque, defaultdict

input = stdin.readline

graph = defaultdict(list)

N = int(input())
X, Y = map(int, input().split())
M = int(input())

for _ in range(M):
    p, c = map(int, input().split())
    graph[p].append(c)
    graph[c].append(p)

# print(graph)


# 촌수 계산이라.. DFS로 하는게 좋겠다!

def dfs(graph, start):
    visited = []
    stack = [start]
    answer = [] 
    if start == X : 
        return 0 
    while stack:        
        node = stack.pop()

        if node not in visited: 
            visited.append(node)
            stack.extend(reversed(graph.get(node)))

        if X in visited:
             return len(visited)-1
            # return visited
    
    return -1

print(dfs(graph,Y))