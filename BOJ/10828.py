from sys import stdin
input = stdin.readline

stack = [] 


N = int(input())

for _ in range(N):
    
    command = input().rstrip()

    if "push" in command:
        _, X = command.split()

        stack.append(int(X))
    
    elif command  == "top":
        if len(stack) == 0 :
            print(-1)
        else: 
            print(stack[-1])
    
    elif command == "size":
        print(len(stack))
    
    elif command == "empty":
        if len(stack) == 0 :
            print(1)
        
        else:  print(0)
        
        
    elif command == "pop":
        if len(stack) == 0 : 
            print(-1)

        else: 
            print(stack.pop())