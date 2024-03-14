from sys import stdin
import sys
sys.setrecursionlimit(10**7)

input = stdin.readline

need_visited = [(0,0)]
visited = []
answer = []

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x,y):

    x,y = need_visited.pop()
    visited.append((x,y))


    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]


        if 0 <= nx < N and 0 <= ny < M:
            if nx == N - 1 and ny == M - 1:
                visited.append((nx,ny))
                return
            elif maze[nx][ny] == "1" and (nx, ny) not in visited:
                need_visited.append((nx,ny))
                answer.append(1)
                dfs(nx,ny)

    return len(visited) ,len(answer), visited

    # return len(visited), visited
    # for x in range(N):
    #     for y in range(M):
    #         for i in range(4):
    #             nx = x + dx[i]
    #             ny = y + dy[i]
    #
    #             if 0 <= nx < N and 0 <= ny < M:
    #                 if maze[nx][ny] == "1" and (nx,ny) not in visited:
    #                     if nx == N - 1 and ny == M - 1:
    #                         continue
    #                     else:
    #                         visited.append((nx,ny))
    #                         dfs()
    #
    #
    # return len(visited)


if __name__ == "__main__":
    N, M = map(int, input().split())
    maze = [input().strip() for _ in range(N)]
    # answer = 1
    print(dfs(0,0))

