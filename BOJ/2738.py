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
for idx in range(N): # 2차원 배열이라는걸 간과했다!
    sum = N_matrix[idx] + M_matrix[idx]
    result.append(sum)
    if idx == N-1:
        result.append(sum)
        result = []

print(result)
    # if idx == N-1:
    #     total.append(result)
    #     result = []

print(total)
# for n, m in zip(N_matrix,M_matrix):
#     sum = n + m
#     result.append(sum)
#     if sum == N:
#         total.append(result)

# print(*total)




