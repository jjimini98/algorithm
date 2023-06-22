from sys import stdin

input = stdin.readline

N = int(input())
visit = sorted([int(input()) for _ in range(N)],reverse=True)
total = 0

for idx, tip in enumerate(visit):
    t = tip - ((idx+1) -1)
    if t <= 0:
        t = 0
    total += t

print(total)