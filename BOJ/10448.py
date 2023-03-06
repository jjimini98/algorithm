from sys import stdin
from itertools import combinations_with_replacement

input = stdin.readline

for _ in range(int(input())):
    K = int(input())
    answer = 0 
    tri = [ i*(i+1)//2 for i in range(1,K//2+1)] 

    for com in combinations_with_replacement(tri, 3):
        if sum(com) == K:
            answer = 1
            break

    print(answer)
    

    