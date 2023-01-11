from sys import stdin
from itertools import combinations


input = stdin.readline

nanjaeng = [ int(input()) for _ in range(9)]

for combi in combinations(nanjaeng, 7):
    if sum(combi) == 100:
        for i in sorted(combi):
            print(i)
    
        break