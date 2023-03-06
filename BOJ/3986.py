from sys import stdin

input = stdin.readline
answer = 0 
for _ in range(int(input())):
    string = input().rstrip()
    stack = [] 
    for x in string:
        if x not in stack: 
            stack.append(x)
        else:
            if stack[-1] == x: 
                stack.pop()
            else:
                stack.append(x)
    
    if len(stack) == 0 :
        answer += 1

print(answer)