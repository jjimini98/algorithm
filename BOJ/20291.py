from sys import stdin
from collections import defaultdict

input = stdin.readline

extender = defaultdict(int)

for _ in range(int(input())):
    _,ex = input().rstrip().split(".")
    extender[ex] += 1


for name,cnt in sorted(extender.items(),key= lambda x : x[0]):
    print(name, cnt)



