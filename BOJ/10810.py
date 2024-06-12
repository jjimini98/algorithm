from sys import stdin

input = stdin.readline

N,M = map(int, input().split())

bucket = [ 0 for _ in range(N)]

for _ in range(M):
    i , j , k = map(int, input().split())
    for idx in range(i-1 , j):
        bucket[idx] = k
    
answer = ''
for idx in range(N):
    answer += str(bucket[idx])
    answer += ' '

print(answer)