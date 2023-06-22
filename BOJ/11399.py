from sys import stdin

input = stdin.readline

N = int(input())
bank = sorted(list(map(int,input().split())))


time = 0
arr = []
for w in bank:
    time += w
    arr.append(time)

print(sum(arr))