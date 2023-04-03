

# 정확성 통과, 효율성 실패 
# def solution(n):
#     arr = [0,1,0,2,1]
#     if n <= 4:
#         return arr[n]
    
#     # n이 5 이상 
#     arr = arr + [0]  * (n - 4)

#     for i in range(5,(n//2)+1):

#         if i % 2 == 0 :
#             arr[i] = arr[i // 2]
        
#         else:
#             arr[i] = arr[i-1] + 1 

#     return arr[n]  


# DP는 너무 어렵다.
def solution(n):
    cnt = 1 
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = n - 1
            cnt += 1
    return cnt

if __name__ == '__main__':
    # print(solution(100000000))
    print(solution(5000))

    