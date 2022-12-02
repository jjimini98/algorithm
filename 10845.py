from sys import stdin
from collections import deque

input = stdin.readline

queue = deque([])


N = int(input())

for _ in range(N):
    
    command = input().rstrip()

    if "push" in command:
        _, X = command.split()

        queue.append(int(X))
    
    elif command  == "top":
        if len(queue) == 0 :
            print(-1)
        else: 
            print(queue[-1])
    
    elif command == "size":
        print(len(queue))
    
    elif command == "empty":
        if len(queue) == 0 :
            print(1)
        
        else:  print(0)
        
    elif command == "pop":
        if len(queue) == 0 : 
            print(-1)

        else: 
            print(queue.popleft())

    elif command == "front" : 
        if len(queue) == 0 : 
            print(-1)

        else: 
            print(queue[0])
    
    elif command == "back" : 
        if len(queue) == 0 : 
            print(-1)

        else: 
            print(queue[-1])