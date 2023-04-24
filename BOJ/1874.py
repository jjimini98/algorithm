from sys import stdin
from collections import deque
input = stdin.readline

N = int(input())
wanted = deque([int(input()) for _ in range(N)])
answer = [] 
i = 1 
stack = [] 
stack.append(i)
answer.append("+")

while wanted :

    if i > N:
        break
    if len(stack) == 0 :
        stack.append(std+1)

    if stack[-1] == wanted[0]:
        wanted.popleft()
        std = stack.pop()
        answer.append("-")
    else:
        i += 1 
        stack.append(i)
        answer.append("+")
    

if i == N : 
    for x in answer:
        print(x)
else:
    print("NO")

