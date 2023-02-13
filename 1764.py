from sys import stdin

input = stdin.readline

N, M = map(int, input().split())

listen = set(input().rstrip() for _ in range(N))

see = set(input().rstrip() for _ in range(M))


inter = listen & see 

print(len(inter))
for i in sorted(inter):
    print(i)

