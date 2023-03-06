from sys import stdin
from collections import deque 

input = stdin.readline


deq = deque([])

def push_front(X):
    deq.appendleft(X) 

def push_back(X):
    deq.append(X)


def pop_front():
    if size() == 0 : 
        print(-1)
    else: 
        item = deq.popleft()
        print(item)

def pop_back(): 
    if size() == 0:
        print(-1)
    else: 
        item = deq.pop() 
        print(item)

def size():
    return len(deq)

def empty():
    if len(deq) == 0 :
        print(1)
    else:
        print(0)

def front():
    if size() == 0 : 
        print(-1)
    else: 
        print(deq[0])

def back():
    if size() == 0 :
        print(-1)
    else: 
        print(deq[-1]) 


N = int(input())

for _ in range(N):

    command = input().rstrip()


    if command == "pop_front":
        pop_front()
    
    elif command == "pop_back":
        pop_back()
    
    elif command == "size":
        print(size())
    elif command == "empty":
        empty()

    elif command == "front" : 
        front()
    
    elif command == "back":
        back()

    else:
        cmd, num = command.split()
        
        if cmd == "push_front":
            push_front(int(num))
        else:
            push_back(int(num))