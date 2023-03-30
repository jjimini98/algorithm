# 반타작 코드 
# from math import log2
# def solution(n,a,b):
#     answer = int(log2(n))

#     while answer:
#         n = n // 2  
 
#         if (a <= n and b <= n):
#             answer -= 1 

#         elif (a > n and b > n) : 
#             n = n + (n//2)
#             # print(n)
#             answer -= 1 
        
#         elif (a <= n and b > n) or (a > n and b <= n):
#             return answer 

#     return 1



# 정답코드 
def solution(n,a,b):
    answer = 0

    x = min(a,b)
    y = max(a,b)

    while True:
        answer +=1
        x = find_team(x)
        y = find_team(y)
        if x==y:
            return answer

def find_team(n):
    return (n+1)//2

# 수정중인 코드 
# from math import log2

# def solution(n,a,b):    

#     answer = int(log2(n))  
#     origin = n
#     Flag = False

#     while answer:
#         n = n // 2  

#         if (a <= n and b <= n):
#             answer -= 1 

#         # elif (a <= n and b <= n) and n != origin: 
#         #     n = n // 2  
#         #     answer -= 1 

#         elif (a > n and b > n) : 
#             # n = n + 2 
#             Flag = True 
#             answer -= 1 
        
#         elif (a <= n and b > n) or (a > n and b <= n):
#             return answer 
        
#     if Flag == True :
#         print(n)

#     return 1

if __name__ == '__main__': 
    # n = 8
    # a = 7
    # b = 4
    n = 16
    a = 9
    b = 12
    print(solution(n,a,b))