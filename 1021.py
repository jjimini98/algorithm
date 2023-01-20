from sys import stdin
from collections import deque

input = stdin.readline

N,M = map(int, input().split())
nums = list(map(int, input().split()))

q = deque([x for x in range(1, N+1)])
answer = 0

def left(queue : deque) -> deque:
    item = queue.popleft()
    queue.append(item)
    return queue

def right(queue : deque) -> deque:
    item = queue.pop()
    queue.appendleft(item)
    return queue


for n in nums:
    idx = q.index(n)

    while True:
        if q[0] == n:
            q.popleft()
            break 

        if idx >= len(q)-idx:
            q = right(q)
            answer += 1
        
        else: 
            q = left(q)
            answer += 1
    
print(answer)