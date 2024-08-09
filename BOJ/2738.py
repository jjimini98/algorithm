from sys import stdin

input = stdin.readline

N,M = map(int,input().split())

N_matrix = []
M_matrix = []
for _ in range(N):
    row = list(map(int,input().split()))
    N_matrix.append(row)

for _ in range(N):
    row = list(map(int,input().split()))
    M_matrix.append(row)


total = []
result = []

for n , m in zip(N_matrix,M_matrix):
    for i , j  in zip(n,m):
        sum = i+j
        result.append(sum)
    if result not in total:
        total.append(result)
        result = []
    else:
        pass



for to in total:
    print(*to)
