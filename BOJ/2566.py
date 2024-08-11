from sys import stdin

input = stdin.readline

arr = []
for _ in range(9):
    lis = list(map(int, input().split()))
    arr.append(lis)

row = 0
col = 0
max_value = 0

for idx , li in enumerate(arr):

    if max(li) >= max_value:
        max_value = max(li)
        row = idx +1
        col = li.index(max_value)

print(max_value)
print(row, col+1)

