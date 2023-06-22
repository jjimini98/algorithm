from sys import stdin
from collections import deque
input = stdin.readline

N = int(input())
price = deque(sorted([int(input()) for _ in range(N)],reverse=True))
def divider(arr):
    new = []
    s = len(arr) // 3
    for _ in range(s):

        tmp = []

        tmp.append(arr[0])
        tmp.append(arr[1])
        tmp.append(arr[2])

        arr.popleft()
        arr.popleft()
        arr.popleft()

        new.append(tmp)

    new.append(list(arr))
    return new

total = 0
new_a = divider(price)

for i in new_a:
    if len(i) == 3:
        total += sum(i[:2])
    else:
        total += sum(i)

print(total)



