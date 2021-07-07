# 4153. 직각삼각형

while True:

    lis = list(map(int, input().split(" ")))
    sum = 0 

    if 0 not in lis:
        lis = sorted(lis)
        big = lis[2]
        for x in range(0,2):
            sum += lis[x]**2 
        
        if sum == big**2 : print("right")
        else : print("wrong")    
    else: break 
