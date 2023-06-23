from sys import stdin

input = stdin.readline



arr = [i for i in range(1,31)]

for _ in range(28):
    ok = int(input())
    arr.remove(ok)


for i in arr:
    print(i)