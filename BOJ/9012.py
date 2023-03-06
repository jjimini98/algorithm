from sys import stdin

input = stdin.readline

for _ in range(int(input())):
    stack = [] 
    flag = 0 
    
    data = input().rstrip()

    for i in range(len(data)):
        if data[i] == "(":
            stack.append("(")

        else: 
            if len(stack) == 0: 
                flag = 1 
            
            else: 
                stack.pop()



    if len(stack) !=0 : 
        print("NO")
    elif flag == 1 :
        print("NO")
    else: 
        print("YES")
