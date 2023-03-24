from sys import stdin
from collections import deque

input = stdin.readline

N = int(input())
graph = [list(map(int,input().strip())) for _ in range(N)]
answer = [] 

dx = [-1,1,0,0]
dy = [0,0,1,-1]


def bfs(graph, x, y):

    queue = deque([(x,y)])
    graph[x][y] = 0 
    cnt = 1

    while queue:
        x,y = queue.popleft()
        
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = 0 
                cnt += 1
                queue.append((nx,ny))

    return cnt




for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            answer.append(bfs(graph, i , j))


print(len(answer))
for x in sorted(answer):
    print(x)





# def bfs(graph, x,y):
#     queue = deque([(x,y)])
#     cnt = 0 

#     while queue:

#         x,y =  queue.popleft()
#         visited.append((x,y))

#         if x >= N or x < 0 or y >= N or y <0 : 
#             continue

#         if graph[x][y] == 1: 
#             visited.append((x,y))
#             cnt += 1

#             for i in range(4):
#                 nx = dx[i] + x
#                 ny = dy[i] + y
                
#                 if nx >= N or nx < 0 or ny >= N or ny <0 : 
#                     continue
#                 if graph[nx][ny] == 1:
#                     cnt += 1
        
#     return cnt 



# for i in range(N):
#     for j in range(N):
        
#         if graph[i][j] == 1 and (i,j) not in visited:
#             answer.append(bfs(graph,i,j))


# print(answer)
