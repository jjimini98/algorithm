from sys import stdin

input = stdin.readline

N, K = map(int, input().split())
lis =[] 

def reverse_(result : int) -> str : 
    result = list(str(result))[::-1]
    return int(''.join(result))

for i in range(1,K+1):
    lis.append(reverse_(N*i))


print(max(lis))