from sys import stdin
from collections import defaultdict, deque

input = stdin.readline

N,M,V = map(int, input().split(" "))

graph = defaultdict(list)

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def dfs(graph : dict, s_node : int): 
    visited = []
    stack = [s_node]

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.append(node)
            try : 
                stack.extend(sorted(graph.get(node))[::-1])
            except: 
                continue
    return visited


answer = dfs(graph, V)
print(*answer)

def bfs(graph, s_node):
    visited = [] 
    queue = deque([s_node])
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)   
            try: 
                queue.extend(sorted(graph.get(node)))
            except: 
                continue

            
    return visited

answer = bfs(graph,V)
print(*answer)

    