from sys import stdin

input = stdin.readline

N,M = map(int, input().split())

bucket = [ i for i in range(1,N+1)]

for _ in range(M):
    i , j = map(int, input().split())
    bucket[i-1], bucket[j-1] = bucket[j-1], bucket[i-1]
    
answer = ''
for idx in range(N):
    answer += str(bucket[idx])
    answer += ' '

print(answer)