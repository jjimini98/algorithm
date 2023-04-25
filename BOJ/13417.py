from sys import stdin
from collections import deque

input = stdin.readline

for _ in range(int(input())):
    N = int(input())
    cards = input().split()
    std = cards[0]
    answer = deque([std])
    
    for i in range(1,N):
        if ord(cards[i]) > ord(min(answer)):
           answer.append(cards[i])
        else:
            answer.appendleft(cards[i])

    print(''.join(answer))