# 런타임 에러 + 시간초과
# from itertools import product,combinations

# def solution(A,B):
#     answer = 0

#     answer += min(A) * max(B)
#     answer += min(B) * max(A)

#     A.remove(min(A))
#     A.remove(max(A))
#     B.remove(min(B))
#     B.remove(max(B))



#     if len(A) >= 1:
#         tmp = [] 
#         for pro in combinations(product(A,B),len(A)):
#             try:
#                 if pro[0][0] == pro[1][0] or pro[0][1] == pro[1][1]: 
#                     continue
            
#                 else:
#                     for x in pro:
#                         answer += x[0] * x[1]
#                     tmp.append(answer)

#             except:
#                 answer += pro[0][0] * pro[0][1]
#                 tmp.append(answer)

#         return min(tmp)
#     else:
#         return answer



def solution(A,B):
    answer = 0

    A = sorted(A,reverse=True)
    B = sorted(B)
    
    while True:
        if len(A) == 0 :
            return answer

        answer += A[0] * B[0]
        A.pop(0)
        B.pop(0)
    # return answer



if __name__ == '__main__': 
    A = [1,4,2]
    B = [5,4,4]
    print(solution(A,B))