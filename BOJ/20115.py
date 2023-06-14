from sys import stdin

input = stdin.readline



N = int(input())
drinks = sorted(list(map(int, input().split())),reverse= True)

answer = drinks[0]

for i in range(1,N):
    answer += drinks[i] / 2


print(answer)


