from sys import stdin

input = stdin.readline

for _ in range(int(input())):

    logger = input().rstrip()
    t = logger.replace(">",'').replace("<","").replace("-",'')
    password = ['' for _ in range(len(t))]
    idx = 0 
    for log in logger:
        if log == ">":
            idx += 1 

        elif log == "<" and idx > 0:
            idx -= 1 
            tmp = password[idx: ]
            password = password[:idx]
            password.append('')
            password = password + tmp 

        elif log == "-":
            password.pop(idx-1)

        else:
            if log not in ["<",">","-"]:
                password[idx] = log
                idx += 1 
    
    print(''.join(password))
